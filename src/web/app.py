from flask import Flask, request, render_template, jsonify
from test import generate_quest
from pathlib import Path
from flask_cors import CORS
import re
import time
import os
import psutil
from datetime import datetime

# Track server start time for uptime calculation
server_start_time = datetime.now()
request_count = 0

app = Flask(__name__, template_folder=str(Path(__file__).parent / "templates"))
CORS(app)  # Enable CORS for all routes

@app.route("/", methods=["GET"])
def read_root():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_endpoint():
    """Generate a quest based on prompt parameter"""
    global request_count
    # Expect JSON input with a "prompt" key
    data = request.get_json()
    prompt = data.get("prompt")
    
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    try:
        # Track performance
        start_time = time.time()
        
        # Generate quest using the provided function
        quest = generate_quest(prompt)
        
        # Clean up the response
        if isinstance(quest, str):
            # Extract just the quest for the given prompt
            pattern = rf'{{\s*"prompt":\s*"{prompt}",\s*"quest":\s*"([^"]+)"\s*}}'
            match = re.search(pattern, quest, re.IGNORECASE)
            
            if match:
                quest = match.group(1).strip()
            else:
                # Fallback cleaning if regex doesn't match
                quest = quest.split('{"prompt":')
                for part in quest:
                    if prompt.lower() in part.lower():
                        try:
                            # Try to extract just the quest part
                            quest_part = part.split('"quest":')[1]
                            quest_part = quest_part.split('}')[0]
                            quest = quest_part.strip('" ').strip()
                            break
                        except:
                            continue
        
        if not quest or quest == prompt:
            return jsonify({"error": "Failed to generate a valid quest"}), 500
        
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        
        # Increment request counter
        request_count += 1
            
        return jsonify({
            "quest": quest,
            "prompt": prompt,
            "elapsed_time": elapsed_time
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/status", methods=["GET"])
def status_endpoint():
    """Return information about the API and model"""
    try:
        # Calculate uptime
        uptime_seconds = (datetime.now() - server_start_time).total_seconds()
        
        # Get system stats
        try:
            cpu_percent = psutil.cpu_percent()
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
        except:
            cpu_percent = "N/A"
            memory_percent = "N/A"
        
        # Model info - for the real GPT-2 model
        model_name = "fine-tuned-gpt2-quest-generator"
        
        return jsonify({
            "status": "running",
            "version": "1.0.0",
            "model": {
                "name": model_name,
                "loaded": True,
                "uptime_seconds": uptime_seconds
            },
            "system": {
                "cpu_percent": cpu_percent,
                "memory_percent": memory_percent,
                "total_requests": request_count
            },
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# For backward compatibility
@app.route("/generate_quest", methods=["POST"])
def generate_quest_endpoint():
    """Legacy endpoint that redirects to /generate"""
    return generate_endpoint()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
# QuestForge - Game Quest Generator API

QuestForge is a game quest generation system that uses a fine-tuned GPT-2 model to create engaging and immersive quest descriptions for games based on simple prompts.

## What This Project Does

QuestForge is designed to help game developers and designers quickly generate creative quest ideas for their games. The system:

1. **Accepts simple prompts** - Just provide a keyword or concept like "dragon", "forest", or "necromancer".
2. **Generates immersive quests** - The system will create detailed quest descriptions. 
3. **Uses a fine-tuned language model** - The system leverages a fine-tuned GPT-2 model specifically trained on game quest data.
4. **Exposes the model via a web API** - The model is available through an easy-to-use API with both programmatic and web interfaces

This tool could be integrated into game development workflows to speed up quest creation, provide inspiration during creative blocks, or serve as a foundation for more complex quest systems.

## Dataset Information

### Source & Processing

The dataset consists of over 500 quest descriptions used to fine-tune the GPT-2 model. The data includes:

- **Core examples (35)**: Carefully handcrafted quest descriptions that establish the baseline style and structure
- **Extended dataset (500+)**: Additional quest examples collected and formatted for training

The data processing pipeline involved:
1. Collecting initial seed quest examples
2. Formatting each quest with a consistent JSON structure: `{"prompt": "keyword", "quest": "description"}`
3. Quality control to ensure each quest follows gaming best practices
4. Fine-tuning the GPT-2 model on this dataset

Each quest was designed to include key gaming elements:
- Player-centric design
- Clear gameplay loops
- Meaningful progression and rewards
- Engaging challenges
- Varied quest archetypes (combat, exploration, puzzle-solving, etc.)

The dataset is stored in two main files:
- `dataset.json` - Core dataset used for initial training
- `full_quests.jsonl` - Extended dataset with 500+ examples

## How to Run QuestForge

### Prerequisites

- Python 3.7 or higher
- Pip package manager
- 4GB+ of RAM (for running the model)
- Git

### Installation and Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/SHANMUGHA-PRIYAN-SK/QuestForge.git
   cd questforge
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask API server:
   ```bash
   cd src/web
   python app.py
   ```

4. Access the web interface at http://localhost:8000

### Running with Docker

For a containerized deployment:

1. Build the Docker image:
   ```bash
   docker build -t questforge .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 questforge
   ```

3. Access the web interface at http://localhost:8000

### API Usage

#### Generate a Quest

**Endpoint**: `POST /generate`

**Request**:
```json
{
  "prompt": "dragon"
}
```

**Response**:
```json
{
  "quest": "Slay the ancient dragon Vrothgar, who guards the cursed hoard in the Emberfall Peaks.",
  "prompt": "dragon",
  "elapsed_time": 0.8531
}
```

#### Check API Status

**Endpoint**: `GET /status`

**Response**:
```json
{
  "status": "running",
  "version": "1.0.0",
  "model": {
    "name": "quest-generator-gpt2",
    "loaded": true,
    "uptime_seconds": 3600
  },
  "system": {
    "cpu_percent": 12.5,
    "memory_percent": 45.2,
    "total_requests": 25
  },
  "timestamp": "2025-04-17T20:15:30.123456"
}
```

## Sample Inputs and Outputs

### Example 1: Simple Monster Quest

**Input**: "dragon"  
**Output**:
```
Slay the ancient dragon Vrothgar, who guards the cursed hoard in the Emberfall Peaks. Navigate through treacherous volcanic caverns filled with dragonkin minions and fire traps. Collect three dragon tears to forge a dragonbane weapon necessary to penetrate Vrothgar's scales. The final battle features multiple phases where you must target specific weak points as the dragon changes attack patterns. Success rewards you with the Dragon Soul Amulet that grants fire resistance and the ability to summon a small drake companion.
```

### Example 2: Mystical Location

**Input**: "crystal cavern"  
**Output**:
```
Explore the Crystal Cavern to find the Heartstone before it shatters from overuse. Deep within the glittering maze of the cavern, navigate through living crystal formations that shift and change when exposed to different types of light. Battle crystalline elemental guardians that shatter into smaller minions when damaged. Collect crystal fragments of different colors to create a harmonic resonance that opens the path to the Heartstone chamber. The reward includes the Prismatic Crystal staff that can manipulate light-based illusions and unlock hidden paths in future quests.
```

### Example 3: Complex Narrative

**Input**: "shadow titan"  
**Output**:
```
You must venture into the Shadow Realm to face the forgotten Titan of Darkness. Once a guardian of balance, the Shadow Titan has been corrupted by void energy and now threatens to engulf the mortal world in eternal night. Battle through the labyrinthine Shadow Caves, solving ancient puzzles that reveal the Titan's weakness. In the final confrontation, you'll need to redirect beams of pure light to break the corruption while dodging devastating shadow attacks that can instantly kill you. Success will earn you the Titan's Shadowplate armor, which grants stealth abilities and resistance to dark magic.
```

## Notes on Future Improvements

Given more time and resources, we would make the following enhancements:

### Model Improvements
1. **Fine-tune on larger datasets**: Collect 5,000+ quest examples across more game genres
2. **Model quantization**: Optimize the model for faster inference on CPU by quantizing to 8-bit precision
3. **Training strategy**: Implement a more sophisticated training approach with reinforcement learning from human feedback (RLHF)
4. **Larger models**: Experiment with larger base models like Llama 3 for more creative and coherent outputs
5. **Add more gameplay elements like**:
   - Combat encounters with varied enemy types
   - Exploration of interesting locations
   - Player rewards and progression
   - Epic boss battles
   - Plot twists and narrative hooks

### API Enhancements
1. **Authentication**: Add API key authentication for security
2. **Rate limiting**: Implement request rate limiting to prevent abuse
3. **Advanced parameters**: Allow more control over generation parameters like creativity, length, and quest type
4. **Caching layer**: Add Redis caching for frequently requested prompts
5. **Async processing**: Implement asynchronous processing for better handling of multiple requests

### User Interface
1. **Quest customization**: Allow users to specify quest difficulty, length, and theme
2. **Quest templates**: Provide pre-defined templates for specific quest types
3. **Interactive editing**: Add the ability to regenerate specific parts of a quest
4. **Export options**: Allow exporting quests in different formats (JSON, Markdown, etc.)

### Game Integration
1. **Unity/Unreal plugins**: Create plugins for popular game engines
2. **Quest structure markup**: Add structured output format for direct integration with quest systems
3. **NPC dialogue generation**: Extend the system to generate related NPC dialogue
4. **World building connections**: Generate connected quests that form a coherent narrative

## License

This project is under development phase only.

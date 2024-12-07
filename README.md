
# ❎🅾️ Tic-Tac-Toe Game with Hand Tracking

A fun and interactive Tic-Tac-Toe game that combines computer vision, hand gestures, and AI for a unique gameplay experience. The project utilizes **OpenCV**, **Mediapipe**, and **Streamlit** for real-time hand tracking and gesture detection, along with **Pygame** for sound effects.

---

## 🚀 Features

- **Hand Gesture Controls**: Play Tic-Tac-Toe using hand gestures detected via Mediapipe.
- **AI Opponent**: Play against a smart AI opponent.
- **Real-time Feedback**: See your moves on a live webcam feed.
- **Sound Effects**: Enjoy dynamic sound effects for moves, wins, and restarts.
- **Score Tracking**: Keep track of scores and determine the winner after 5 matches.
- **User-Friendly Interface**: Built with Streamlit for an engaging UI.

---

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For creating an interactive UI.
- **OpenCV**: For webcam feed and drawing the game grid.
- **Mediapipe**: For hand tracking and gesture recognition.
- **Pygame**: For adding sound effects.
- **Numpy**: For mathematical operations.

---

## 📋 Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8+
- A webcam for real-time gesture tracking.

## 📂 Project Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-hand-gesture.git
   cd tic-tac-toe
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Sound Files**
   - Place the following sound files in the appropriate path (e.g., `E:/Web Development/Tic-Tac-Toe-Game/sound/`):
     - `move.wav`: Sound for player moves.
     - `win.wav`: Sound for when a player wins.
     - `start_sound.wav`: Sound for restarting the game.

4. **Add Icon and Image Assets**
   - Place the `Tic-tac-toe.png` icon in the specified directory (e.g., `E:/Web Development/Tic-Tac-Toe-Game/images/`).

5. **Run the Application**
   ```bash
   streamlit run tic_tac_toe.py
   ```

---

## 🎮 How to Play

1. **Start the Game**:
   - Open the Streamlit app.
   - A webcam feed will appear, along with a Tic-Tac-Toe grid.

2. **Make a Move**:
   - Use your hand gesture to interact with the grid.
   - Pinch your thumb and index finger to "click" on a cell.

3. **Game Rules**:
   - Take turns playing as "X".
   - The AI will play as "O".
   - Win by aligning three marks in a row, column, or diagonal.

4. **Win the Match**:
   - The first player to reach 5 wins is the overall winner.

---

## 🖼️ User Interface

### **Section 1: Scoreboard**
- Displays real-time scores for Player (X) and AI (O).
- Updates automatically after each round.

### **Section 2: Webcam Feed**
- Displays the live video feed.
- Highlights the selected cell and shows the game grid.


## 🐞 Troubleshooting

1. **Webcam Not Detected**:
   - Ensure your webcam is connected and accessible.
   - Check your system's privacy settings.

2. **Sound Effects Not Playing**:
   - Verify the file paths for `move.wav`, `win.wav`, and `start_sound.wav`.
   - Check your system's audio settings.

3. **Gesture Not Detected**:
   - Ensure your hand is clearly visible to the webcam.
   - Adjust lighting for better hand tracking.


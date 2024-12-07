import streamlit as st  
import cv2
import mediapipe as mp
import numpy as np
import random
import pygame

# Initialize Pygame Mixer for Sound Effects
pygame.mixer.init()
move_sound = pygame.mixer.Sound("E:/Web Developement/Tic-Tac-Toe-Game/sound/move.wav")
win_sound = pygame.mixer.Sound("E:/Web Developement/Tic-Tac-Toe-Game/sound/win.wav")
restart_sound = pygame.mixer.Sound("E:/Web Developement/Tic-Tac-Toe-Game/sound/start_sound.wav")

# Initialize Mediapipe for Hand Tracking
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize the Tic-Tac-Toe grid
grid = [["" for _ in range(3)] for _ in range(3)]
player_turn = True
winner = None
player_score = 0
ai_score = 0
match_count = 0

# Winning score limit
WINNING_SCORE = 5

# Colors for grid and moves
grid_color = (255, 255, 255)
player_color = (0, 255, 0)  # Green for player 'X'
computer_color = (0, 0, 255)  # Red for computer 'O'

# Cell size for drawing
cell_size = 130
window_size = cell_size * 3

# Streamlit Page Configuration
st.set_page_config(
    page_title="Tic-Tac-Toe",
    page_icon="E:\Web Developement\Tic-Tac-Toe-Game\images\Tic-tac-toe.png",
    layout="wide"
)

# Streamlit Layout
st.markdown(
    """
    <h1 style='text-align: center; color: #F39C12;'> ❎🅾️ Tic-Tac-Toe Game
    </h1>
    """,
    unsafe_allow_html=True
)


# Layout with more space between the two main columns
spacer_col1, col1, spacer_col2, col2, spacer_col3 = st.columns([2, 3, 2, 6, 1])

# Section 1: Scoreboard and Status
with col1:
    st.markdown("<h3 style='text-align: left; color: #2980B9;'>🏆 Scores</h3>", unsafe_allow_html=True)
    colm1, spacer_col, colm2 = st.columns([1, 1, 1])
    with colm1:
        player_score_display = st.metric("Player (X)", player_score)
    with colm2:
        ai_score_display = st.metric("AI (O)", ai_score)
    st.markdown("<h3 style='text-align: left; color: #E74C3C;'>🎮Game Status</h3>", unsafe_allow_html=True)
    game_status = st.empty()  # Placeholder for game status
    st.markdown("<hr style='border: 2px solid #95A5A6;'>", unsafe_allow_html=True)
    progress = st.progress(0)  # Initialize progress bar
    restart_game = st.button("🔄 Restart Game")  # Restart button

# Section 2: Webcam Feed
with col2:
    st.markdown("<h3 style='text-align: center; color: #27AE60;'>🎥 Webcam Feed</h3>", unsafe_allow_html=True)
    frame_placeholder = st.empty()
# Function to reset the game
def reset_game():
    global grid, player_turn, winner, match_count
    grid = [["" for _ in range(3)] for _ in range(3)]
    player_turn = True
    winner = None
    match_count += 1
    progress.progress(min(match_count / WINNING_SCORE, 1.0))  # Update progress bar
    pygame.mixer.Sound.play(restart_sound)

# Function to check for a winner
def check_winner():
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != "":
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != "":
            return grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] != "":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != "":
        return grid[0][2]
    if all(cell != "" for row in grid for cell in row):
        return "Draw"
    return None

# Function for AI move
def computer_move():
    available_cells = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == ""]
    if available_cells:
        i, j = random.choice(available_cells)
        grid[i][j] = "O"
        pygame.mixer.Sound.play(move_sound)

# Function to draw the grid and moves
def draw_grid(frame):
    for i in range(4):
        cv2.line(frame, (0, i * cell_size), (window_size, i * cell_size), grid_color, 2)
        cv2.line(frame, (i * cell_size, 0), (i * cell_size, window_size), grid_color, 2)
    for i in range(3):
        for j in range(3):
            x = j * cell_size + cell_size // 2
            y = i * cell_size + cell_size // 2
            if grid[i][j] == "X":
                cv2.putText(frame, "X", (x - 40, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 2, player_color, 3)
            elif grid[i][j] == "O":
                cv2.putText(frame, "O", (x - 40, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 2, computer_color, 3)

# Function to find the grid cell from the fingertip position
def get_grid_cell(x, y):
    col = x // cell_size
    row = y // cell_size
    return int(row), int(col)

# Function to detect a click gesture
def detect_click(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    distance = np.linalg.norm([thumb_tip.x - index_tip.x, thumb_tip.y - index_tip.y])
    return distance < 0.05

# Function to update the scoreboard
def update_score(winner):
    global player_score, ai_score
    if winner == "X":
        player_score += 1
        pygame.mixer.Sound.play(win_sound)
    elif winner == "O":
        ai_score += 1
        pygame.mixer.Sound.play(win_sound)

# Function to display the overall winner after 5 matches
def display_overall_winner():
    if player_score > ai_score:
        return "Player Wins! 🎉"
    elif ai_score > player_score:
        return "AI Wins! 🤖"
    else:
        return "It's a Tie! 🎭"

# Main Game Loop
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if restart_game:  # Check if the restart button is clicked
        reset_game()

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Update real-time scores
    player_score_display.metric("Player (X)", player_score)
    ai_score_display.metric("AI (O)", ai_score)

    # Draw the grid and moves
    draw_grid(frame)

    # Process hand landmarks for gesture detection
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            finger_x = int(index_finger_tip.x * window_size)
            finger_y = int(index_finger_tip.y * window_size)

            row, col = get_grid_cell(finger_x, finger_y)
            if 0 <= row < 3 and 0 <= col < 3:
                cv2.rectangle(frame, (col * cell_size, row * cell_size),
                              ((col + 1) * cell_size, (row + 1) * cell_size), (200, 200, 0), 2)

            if player_turn and detect_click(hand_landmarks.landmark):
                if grid[row][col] == "":
                    grid[row][col] = "X"
                    player_turn = False
                    pygame.mixer.Sound.play(move_sound)

    if not player_turn:
        winner = check_winner()
        if not winner:
            computer_move()
            player_turn = True
        else:
            update_score(winner)

    if winner:
        if match_count >= 5:
            overall_winner = display_overall_winner()
            game_status.markdown(f"<h2 style='color: #16A085;'>{overall_winner}</h2>", unsafe_allow_html=True)
            cap.release()  # End the game after 5 rounds
            break
        else:
            status_text = "Draw!" if winner == "Draw" else f"{winner} Wins!"
            game_status.markdown(f"<h2 style='color: #D35400;'>{status_text}</h2>", unsafe_allow_html=True)
            pygame.time.wait(2000)
            reset_game()

    frame = cv2.resize(frame, (window_size, window_size))  # Resize webcam feed to match grid size
    frame_placeholder.image(frame, channels="BGR")

cap.release()
cv2.destroyAllWindows()




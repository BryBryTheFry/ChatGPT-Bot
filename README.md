# ChatGPT-Bot
A program that allows for the user to have a conversation with ChatGPT.

# Process
1. Transcribe the speech of the user.
2. Detect if the user has asked a question by searching the transcribed text for the trigger word.
3. Use the OpenAI API to get ChatGPT's response.
4. Use TTS to turn ChatGPT's response into audio and play it.

# Transcription
- This process works by simultaneously recording audio and transcribing it
- We use the speech recognition library as it allows for us to obtain audio from the microphone
  - It also allows for detection of when speech has stopped to make the process smoother
- Save the recorded audio to a temporary file to be read by whisper
- We use the whisper library to transcribe the audio obtained from speech recognition
- Whenever the phrase is completed, meaning that a pause in speech has been detected, append the transcribed text to the list

# Playing Audio
- Playing audio is a significantly easier task
- Using libaries we convert a string into a temporary .mp3 file
- The playsound libary allows us to play the audio from the temporary .mp3 file

CROSS-LINGUAL EMOTIONAL VOICE CONVERSION FOR NATURAL DUBBING

Steps:
1. Loaded audio file using pydub from own recorded audio.
2. Transcribe English audio using OpenAI Whisper.
3. Translate transcript to Hindi using Google Translate.
4. Extract a 5-second voice sample for reference.
5. Analyze audio features: pitch (YIN), pitch variance, energy.
6. Synthesize raw Hindi speech using Coqui XTTS with reference voice.
7. Emotion-modulate pitch and energy using pyrubberband & RMS envelope.
8. Save final expressive Hindi audio: output_xtts_emotion.wav

Libraries Used:
- whisper
- googletrans
- librosa, pydub
- Coqui TTS (XTTS)
- pyrubberband
- numpy, scipy

Output Files:
- reference.wav (reference voice clip)
- output_xtts_raw.wav (raw XTTS output)
- output_xtts_emotion.wav (emotion-modulated final result)

Note:
- Exclude `coqui_env/` from Git using `.gitignore`

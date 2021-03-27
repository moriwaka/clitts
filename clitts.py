#!/usr/bin/python3

def synthesize(inputtext, outfile, isssml):
    """Synthesizes speech from the input string of ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/

    Example: <speak>Hello there.</speak>
    """
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    if isssml:
        input_text = texttospeech.SynthesisInput(ssml=inputtext)
    else:
        input_text = texttospeech.SynthesisInput(text=inputtext)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="ja-JP",
        name="ja-JP-Wavenet-D",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open(outfile, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to file {outfile}')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Generate mp3 from SSML or Text')
    parser.add_argument('--ssml', action='store_true', default=False, help='input is SSML')
    parser.add_argument(metavar='input.txt', dest='inputfile', help='input text file')
    parser.add_argument(metavar='output.mp3', dest='output', help='output mp3 file')

    args = parser.parse_args()
    with open(args.inputfile, 'r') as f:
        synthesize(f.read(), args.output, args.ssml)

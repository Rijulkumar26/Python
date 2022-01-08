Hello madiee this is Rijul Kumar, I attempted this assignment by using speech recognition library of python.
As a result, i don't have to build a machine learning model from scratch.
This library provides us with handy and popular public speech recognition APIs (like Google Cloud Speech API, IBM Speech To Text, etc.).
I am going to use Google Speech Recognition here.

So first of all i have converted .m4a file to .wav file using external tool which could have also been done in python itself. 
Then i have mounted the .wav file on my google colab.
Next i downloaded speech recognition and pydub packages and imported the libraries required.
After that i initialized r as my speech recognizer.

As i want to perform speech recognition of a long audio file i have used split_on_silence() function from pydub.silence module to split audio data into chunks on 
silence.

min_silence_len parameter is the minimum length of a silence to be used for a split which i have set to 500 milliseconds.

silence_thresh is the threshold in which anything quieter than this will be considered silence. I have set it to the average dBFS-8.
keep_silence argument is the amount of silence to leave at the beginning and the end of each chunk detected in milliseconds.

After that, we iterate over all chunks and convert each speech audio into text and concatinating all of them.

Now as we can see there are some unknown value error which are mainly from Google Speech Recognition which we are using and the reason being noise disturbance and there
are also some misinterpretation because of variation in pronunciation of words.

To calculate number of pauses i have just subtracted 1 from total number of audio chunks as i am separating audio chunks on the basis of pauses.

Afterwards i have created a dictionary with key as the words of the full text which i have obtained previously and value as the number of times they have repeated.

At the end i have printed all the words and the number of times they have appeared and further printed all the words which appears only once and in next line printed 
the words which appear more than once.
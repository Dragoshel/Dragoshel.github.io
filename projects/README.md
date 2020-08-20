## Story
  Tell a story
  Jeremiah Dedon and the secret blinking morse code.
## Table of contents
  Write table of contents
  
## Introuction
	Today you don't have to worry too much about the methods of concealing a message ...
	Goner are the days when you had to ponder over the great selection of invisible inks
	to hide your secret affairs. You no longer have to worry about the safety of your
	servant when shaving its head with razorblades in order to write a message on his scalp,
	so that no one will bother to check once the hair grows back.

	"So how would I do it today? I don't want to be held back from this awesome activity
	because of some outdated tools. I want to get my thoughts across without anyone
	getting the better of me" - you may impaciently say. As for most questions in life,
	computers is the  answer. More specifically, encoding a digital message into
	another digital file using a bit of ingenuity, tricks and algorithms. Getting the message
	out will be as simple as reversing the hiding action, removing the hassle and inconvenience
	in the process. Thus, we gather a lot of advantages from digital encoding:
		- Very hard to decode if one doesn't know the method of hiding.
		- Reliable, as the encoded file is persistent and doesn't change with time.
		- No limitations. It's entirely possible that the message may very well be an image, a
		document, or anything other than plain text. Picture this... hiding an image inside another
		image :)
		- It profundely reduces noticeble alterations to the original image, in contrast
		to physical steganography where the paper encoded presents visible damage or irregularities.
		- Easy

	Clearly, there's an overwhelimg superiority of digital steganography over traditional means.
	With so many advanatges backing it up, it's only logical that people will want to use it.
	There's allready a handful of tools out there capable of superbly hiding anything into images,
	implementing all of the advantages mentioned above (Some of the tools are: "steghide", "jsteg"
	or "Hide'N'Steg"). This means that anyone with a home computer can get on board with hiding
	texts, and those programs will greatly imporve the experience of doing so. 

	Alright, now you're interested in the subtle arts of hiding things in plain sight and want to
	learn more about it... How do you use it? What are the possibilites and what are the downsides?
	And how is such a seamingly complex process achieved? I will begin addressing all of those
	questions and give a top-down explanation of how this system works, as well as how it can be
	implemented using computer code.

## Explanation
Without wasting anymore time, let's jump straight into what makes computer steganography such an amazing field to work in. Grab your linux distro and terminal of choice, and install "steghide" (a tool of my choice) and let's hide some messages! Here I a text file containing one of the most popular quotes of Geralt from "The Witcher" books, and right beside it, a picture of a cat.

			[Geralt quote text]					[Picture of a cat]

Fire up the terminal, and let's embed the text file right inside that cat.jpeg.
			[Picture of the terminal with the command and arguments to embed a message into a picture]
			steghide embed -v -cf "cat.jpg" -ef "witcher_quote.txt"

Explanation of the command:
	- steghide is the name of the program we're going to use.
	- the well known -v flag for verbose output gives extra information on what is hapenning behind the hood.
	- the -cf is for "cover file" and the next argument will specify the path of the file you want to embed into. - In this context "cover file" is just a fancy name for our cat image.
	- embed is the first option that steghide need to get as input when you want to hide files.
	- the -ef flag stands for "embed file" and lets you pass the path of the file you want to hide, and in this case it's going to be my witcher quote.

Executing this command will begin the process of embedding the data, and if everything runs smoothly, you should get an output like this:
			[Picture showing output]
Steghide will hide the data directly inside of that image, so be sure you'll have a backup just in case, because you're not getting your original file back.
Now take a look at the modified image! It's so cool, it's marvelous, it's... it's the same image. Remember when I told you the file remains intact and there's no way of telling with the naked eye that there's something hidden inside? That's exactly the point. The integrity of the original file must remain aproximatively the same for the steganographic process to be succsessful. Now, there is not to say that there will be someone stopping you from hiding so much data that you completely eradicate enven the slightest trace of a cat in that image, but it would be quite obvious that you've hidden something secret when your feline buddy looks like the noise of an old cathod tube tv. Additonally, you can hide your texts in audio files.
 
* Why you didn't use c instead of python.
## Implementation
  Write implementation
  
## Conclusion
  Write conclusion
## Future work
  Write future work
## References
  Write references

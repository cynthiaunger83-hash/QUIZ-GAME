questions = ("what sending school is cynthia's", "what is the true statement about bipolar disorder", "what is one of the most commonly faked disorders ", "what does POTS mean", "what is the diffrence between DID and OSDD" )
options = (
    ("A. milcreek","B. Fort Le Boeuf", "C. Girard", "D. wattsburg"),
    ("A. Bipolar disorder is juest mood swings", "B. Bipolar effects 2-3 precent of the world", "C. Mainia or Hypomania is fun and exciting", "D. only adults get Bipolar disorder"),
    ("A. Autism", "B. Bipolar disoreder", "C. DID/OSDD", "D. ADHD"),
    ("A. kitchen applinces", "B. Postural Orthostatic Tachycardia Syndrom", "C. Possibly Open Terms Suggestions", "D. Portugal Official Teams System"),
    ("A. there is no diffrence", "B. DID is more in adult hood OSDD is more common in children and teens", "C. DID is truama based and OSDD is not" "D. they are spelled diffrently"),
)
answers = ("A","B","C","B","B")
correct = 0
real_num = 0
question_num = 0 
for question in questions:
   question_num += 1
   print(f"question {question_num}: {questions[real_num]}")
   print(options[real_num][0])
   print(options[real_num][1])
   print(options[real_num][2])
   print(options[real_num][3])
   player_answer = input("pick A B C D -> ").upper()
   if player_answer != "A" or  "B" or "C" or "D":
       print("invalid answer")
       player_answer = input("")
   if player_answer == answers[real_num]:
      player_answer = input("pick A B C D -> ").upper()
      correct += 1
   else:
      print(f"inncorrect, the correct is {answers[real_num]}")
   if question == questions[0]:
        guess_0 = player_answer
   if question == questions[1]:
        guess_1 = player_answer
   if question == questions[2]:
        guess_2 = player_answer
   if question == questions[3]:
        guess_3 = player_answer
   if question == questions[4]:
        guess_4 = player_answer
guessses = (guess_0, guess_1, guess_2, guess_3, guess_4)
print("_-_-_-RESULTS-_-_-_")
print(f"answers: {answers}")
print(f"guesse{guessses}")
print(f"your score is {(correct * 100) // len(questions)}%")

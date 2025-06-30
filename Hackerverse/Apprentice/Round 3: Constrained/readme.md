- What is the best time to play the game? Hm, what could this mean?
- After completing "Round 3: Administrator", we can login as an administrator and we are given a terminal.
  <img width="794" alt="Screenshot 2025-06-30 at 3 37 08 PM" src="https://github.com/user-attachments/assets/fa58e4d4-6947-419a-a949-cf517358d672" />
- After doing some looking around, we have a set of commands and some files.
  
  <img width="393" alt="Screenshot 2025-06-30 at 3 38 07 PM" src="https://github.com/user-attachments/assets/886ce4a9-af49-4323-9108-5b10bc005b6f" />
- If we view the contents of "puzzle.base64", it is encoded in base64. So let's use cyberchef to decode this. We get the code given in "puzzle.html".
- It is obfuscated, so we will deobfuscate it into puzzle_de.html. When inspecting the code, it looks like a space invader game but with some twists.
- The code snippet below shows that the invincibility of the boss depends on bo.iv and that it depends on j3()
  <img width="457" alt="Screenshot 2025-06-30 at 3 45 02 PM" src="https://github.com/user-attachments/assets/cef068d7-042b-400e-8f82-f6b801ac0080" />
- The code below shows j3 and we see that the output depends on the UTC hour of day being between 0x5 (inclusive) and 0x8 (exclusive)

  
  <img width="245" alt="Screenshot 2025-06-30 at 3 46 25 PM" src="https://github.com/user-attachments/assets/f62fdb47-ac34-4be7-a9c4-c72acbcadae4" />
- UTC = GMT, so we should play the game between 5am and 7:59am!

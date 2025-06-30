- When we navigate to the html document, it takes us to the webpage shown below
- <img width="510" alt="Screenshot 2025-06-30 at 3 25 32 PM" src="https://github.com/user-attachments/assets/37ed60ff-2832-46b6-b18f-9a2399f25b78" />
- If we inspect the element, we see a ton of crazy looking javascript code
- <img width="885" alt="Screenshot 2025-06-30 at 3 26 20 PM" src="https://github.com/user-attachments/assets/eea9f6fa-fb1f-474a-aa98-e9df256dcab5" />
- This has been obfuscated, so we can deobfuscate this using an online engine.
- This gives us the code given in "Round 3 Administrator.js"
- We see a section that checks for credentials: 
- <img width="602" alt="Screenshot 2025-06-30 at 3 30 14 PM" src="https://github.com/user-attachments/assets/9e47ca6b-6007-4f88-9a40-c12f06e10dd6" />

- The username should be zs_admin, but upon further inspection, this other test is actually of a hash of the password. We must reverse this to get the original password
- It is a SHA-256 hash, so we can attempt a reverse hash lookup using an online dictionary.
  
- <img width="989" alt="Screenshot 2025-06-30 at 3 33 12 PM" src="https://github.com/user-attachments/assets/0702d705-ae9d-46ef-ba16-b9464238039f" />
- Now we have the credentials!

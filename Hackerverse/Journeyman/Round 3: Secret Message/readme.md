- We have to find the credentials for the IP 192.168.1.100
- After completing Part 3: Administrator, we have the following files in the shell
  
- <img width="393" alt="Screenshot 2025-06-30 at 3 38 07 PM" src="https://github.com/user-attachments/assets/5add3c9b-cbbe-4504-bb3d-abebf5dc7dc0" />

- Let's try to uncover the secret. When we try to view the contents, the output tells us that we should use a decrypt command, which then tells us that we need a key file
- When inspecting the html (of the login screen), we notice a massive amount of gibberish seen below
- <img width="457" alt="Screenshot 2025-06-30 at 4 04 51 PM" src="https://github.com/user-attachments/assets/cca4bb84-142c-4e90-b78b-51a9b0b64237" />

- When inspecting the code for the login screen, this is actually the encrypted script that is used when we login. We can reverse this encryption by reversing the function with the ciphertext as the input.
- This code is given away by the text "decrypt" shown below
- <img width="446" alt="Screenshot 2025-06-30 at 4 08 06 PM" src="https://github.com/user-attachments/assets/fbb121c0-9461-4b17-a15a-3d09887788d2" />

- We can reverse this code using the snippet of code below

- <img width="701" alt="Screenshot 2025-06-30 at 4 09 29 PM" src="https://github.com/user-attachments/assets/30cf553e-9f31-4ffe-a0ee-a2073012d1f1" />

- The decrypted code is shown in the file "decrypted.js"
- When inspecting this code, we see that we must use sudo to decrypt (shown below)

- <img width="665" alt="Screenshot 2025-06-30 at 4 10 48 PM" src="https://github.com/user-attachments/assets/30d46a6a-d712-4022-aacb-4550f6cedbf1" />

- We also see the key that was used

- <img width="696" alt="Screenshot 2025-06-30 at 4 12 10 PM" src="https://github.com/user-attachments/assets/be5d87d0-7c9f-4d63-b805-403b83a8aff5" />

- And we see that we need to specify the key in a file called "private.key"
- <img width="549" alt="Screenshot 2025-06-30 at 4 15 09 PM" src="https://github.com/user-attachments/assets/b648caa3-78e7-40ee-96dc-910b60a603cb" />

- Thus, we need to run the following commands to decrypt
  - ```touch private.key```
  - ```edit private.key``` (add the key "alphaomega123")
  - ```decrypt secret.txt.enc```
 
- Output is shown below and now we have the credentials!
- <img width="417" alt="Screenshot 2025-06-30 at 4 17 01 PM" src="https://github.com/user-attachments/assets/f9d5512c-440c-47a9-b9ef-e2c838946539" />


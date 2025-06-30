- We are given a binary file called binary1 that requires a password.
- Luckily, we can reverse engineer this binary using a tool such as Ghidra to take a look at the code that was used to create this file.
- We see that we have a function that calls verify_password to see if we input the correct password
- <img width="447" alt="Screenshot 2025-06-30 at 2 10 21 PM" src="https://github.com/user-attachments/assets/c19b0a81-84bd-4f31-bd3a-38105525b714" />
<img width="601" alt="Screenshot 2025-06-30 at 2 10 37 PM" src="https://github.com/user-attachments/assets/1455bec8-9f7c-48b5-bab0-d22e5d2bdd76" />

- I like to start these by going backwards. We see that it returns a boolean, and this boolean is obtained when comparing the first 16 bytes of two values.
- One of these values is given by 0x673a257...
- This value is only 8 bytes, not 16. The other 8 will actually be the next value given by 0x3131... because the buffer stores these values right next to eachother and so the comparison will utilize both of these values.
- So, we need to create this 16 byte value. We see that the loop transforms our input in a special way and so need to give an input such that the transformation matches those 16 bytes.
- The tranformation simply iterates through our input and xors each character with the hex value 0x42.
- Xor is associative, so we can figure out our input by reversing the operation. This is given by our python code below.
- <img width="314" alt="Screenshot 2025-06-30 at 2 23 40 PM" src="https://github.com/user-attachments/assets/9a0882d0-e1f7-4681-abc3-765daed3fde8" />

- The output we get is "jmc34gx%ooOVoPss"

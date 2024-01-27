# **Automated Email Sender**

Welcome to the Automated Email Sender project! This project provides a simple script for sending automated emails using Python with the **`smtplib`** and **`schedule`** libraries.

## **Features**

- Send automated emails with a specified subject, message, and recipient.
- Schedule the email sending task to run at a specific time using the **`schedule`** library.

## **How to Run**

1. **Clone the Repository:**
    
    ```bash
    bashCopy code
    git clone [repository_url]
    
    ```
    
2. **Navigate to the Project Directory:**
    
    ```bash
    bashCopy code
    cd automated-email-sender
    
    ```
    
3. **Install Dependencies:**
    
    ```bash
    bashCopy code
    pip install smtplib schedule
    
    ```
    
4. **Replace Email Credentials:**
    - Open the **`email_sender.py`** file.
    - Replace **`your_email@gmail.com`** with your Gmail email address.
    - Replace **`your_email_password`** with your Gmail app password or account password.
5. **Run the Script:**
    
    ```bash
    bashCopy code
    python email_sender.py
    
    ```
    
6. **Customize Email Content:**
    - Modify the **`subject`**, **`message`**, and **`to_email`** variables in the **`job`** function based on your preferences.

## **Customization**

- Adjust the scheduled time and frequency by modifying the **`schedule.every().day.at("10:00").do(job)`** line in the **`email_sender.py`** file.
- Add more complex logic or tasks inside the **`job`** function if needed.

## **Important Note**

- Using email credentials directly in the code may not be secure. For production use, consider using environment variables or a more secure method for storing credentials.
- Ensure you follow the security guidelines of your email provider, and some providers may require you to enable "less secure apps" or generate an "app password."

## **Author**

Jeel patel

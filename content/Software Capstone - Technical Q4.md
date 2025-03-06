# Whiteboarding Question: Notification System  

## Problem Statement  
You are designing a notification system that sends messages through different channels. The system should support multiple types of notifications while ensuring all notifications follow a common structure.  


### **Requirements:**  
- Every notification must have a recipient (who receives the message).  
- Every notification must have a message body.  
- Each notification type must have a `send()` method that prints a formatted message to the console.  
- Different types of notifications format their messages differently:  

  **EmailNotification** should print:  
  ```
  Sending Email to user@example.com:  
  Subject: Important Update  
  Body: "You've got mail!"  
  ```  

  **SMSNotification** should print:  
  ```
  Sending SMS to +1234567890:  
  Message: "New message received!"  
  ```  

  **PushNotification** should print:  
  ```
  Sending Push Notification to user123:  
  Alert: "Check your app for updates!"  
  ```  

- All notifications should log their delivery after being sent. Example:  
  ```
  Notification sent successfully.  
  ```  
- The system should be easily extendable to support new notification types without modifying existing code.  

---

## **Example Expected Usage**
```java
Notification email = new EmailNotification("user@example.com", "Important Update", "You've got mail!");
Notification sms = new SMSNotification("+1234567890", "New message received!");
Notification push = new PushNotification("user123", "Check your app for updates!");

email.send();
sms.send();
push.send();
```

#### **Expected Console Output**
```
Sending Email to user@example.com:  
Subject: Important Update  
Body: "You've got mail!"  
Notification sent successfully.

Sending SMS to +1234567890:  
Message: "New message received!"  
Notification sent successfully.

Sending Push Notification to user123:  
Alert: "Check your app for updates!"  
Notification sent successfully.
```

---

## **Task**
- Design and implement the `Notification` structure so that all notifications share common behavior and data.  
- Ensure that new notification types can be added without modifying existing code.  
- Implement shared functionality (such as logging) in a way that applies to all notifications without duplicating code.  

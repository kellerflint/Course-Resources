# Q4 Solution
### **Step 1: Define the Base Class (`Notification`)**  
- Stores shared data (`recipient`, `message`).  
- Defines the common behavior (`send()` must be implemented in subclasses).  
- Implements a logging feature that all notifications inherit.
  
```java
abstract class Notification {
    protected String recipient;
    protected String message;

    public Notification(String recipient, String message) {
        this.recipient = recipient;
        this.message = message;
    }

    public abstract void send();

    protected void logDelivery() {
        System.out.println("Notification sent successfully.\n");
    }
}
```


### **Step 2: Implement Subclasses for Each Notification Type**  
Each subclass **inherits from `Notification`** and **implements `send()` uniquely**.  

```java
class EmailNotification extends Notification {
    private String subject;

    public EmailNotification(String recipient, String subject, String message) {
        super(recipient, message);
        this.subject = subject;
    }

    @Override
    public void send() {
        System.out.println("Sending Email to " + recipient + ":");
        System.out.println("Subject: " + subject);
        System.out.println("Body: \"" + message + "\"");
        logDelivery();
    }
}

class SMSNotification extends Notification {
    public SMSNotification(String recipient, String message) {
        super(recipient, message);
    }

    @Override
    public void send() {
        System.out.println("Sending SMS to " + recipient + ":");
        System.out.println("Message: \"" + message + "\"");
        logDelivery();
    }
}

class PushNotification extends Notification {
    public PushNotification(String recipient, String message) {
        super(recipient, message);
    }

    @Override
    public void send() {
        System.out.println("Sending Push Notification to " + recipient + ":");
        System.out.println("Alert: \"" + message + "\"");
        logDelivery();
    }
}
```

### **Step 3: Demonstration**

```java
public class NotificationSystem {
    public static void main(String[] args) {
        Notification email = new EmailNotification("user@example.com", "Important Update", "You've got mail!");
        Notification sms = new SMSNotification("+1234567890", "New message received!");
        Notification push = new PushNotification("user123", "Check your app for updates!");

        email.send();
        sms.send();
        push.send();
    }
}
```

### **Expected Console Output**
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

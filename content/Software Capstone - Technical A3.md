# Q3 Solution

```java
// Step 1: Define an Interface
interface PaymentMethod {
    boolean process(double amount);
}

// Step 2: Implement Concrete Payment Methods
class PayPal implements PaymentMethod {
    private String email;
    private String password;

    public PayPal(String email, String password) {
        this.email = email;
        this.password = password;
    }

    @Override
    public boolean process(double amount) {
        System.out.println("Processing PayPal payment of $" + amount + " for " + email);
        return true;  // Simulating success
    }
}

class CreditCard implements PaymentMethod {
    private String cardNumber;
    private String cvv;
    private String billingAddress;

    public CreditCard(String cardNumber, String cvv, String billingAddress) {
        this.cardNumber = cardNumber;
        this.cvv = cvv;
        this.billingAddress = billingAddress;
    }

    @Override
    public boolean process(double amount) {
        System.out.println("Processing Credit Card payment of $" + amount + " for card " + cardNumber);
        return true;  // Simulating success
    }
}

class Bitcoin implements PaymentMethod {
    private String walletAddress;

    public Bitcoin(String walletAddress) {
        this.walletAddress = walletAddress;
    }

    @Override
    public boolean process(double amount) {
        System.out.println("Processing Bitcoin payment of $" + amount + " to wallet " + walletAddress);
        return true;  // Simulating success
    }
}

// Step 3: Checkout Function
public class PaymentProcessor {
    public static void checkout(PaymentMethod paymentMethod, double amount) {
        if (paymentMethod.process(amount)) {
            System.out.println("Payment successful!");
        } else {
            System.out.println("Payment failed!");
        }
    }

    // Step 4: Demonstration
    public static void main(String[] args) {
        PaymentMethod paypalPayment = new PayPal("user@example.com", "securepassword");
        PaymentMethod creditCardPayment = new CreditCard("1234-5678-9012-3456", "123", "123 Main St");
        PaymentMethod bitcoinPayment = new Bitcoin("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa");

        checkout(paypalPayment, 50.00);
        checkout(creditCardPayment, 100.00);
        checkout(bitcoinPayment, 200.00);
    }
}
```

### **Example Usage:**  
```java
public static void checkout(PaymentMethod paymentMethod, double amount) {
    if (paymentMethod.process(amount)) {
        System.out.println("Payment successful!");
    } else {
        System.out.println("Payment failed!");
    }
}

public static void main(String[] args) {
    PaymentMethod paypalPayment = new PayPal("user@example.com", "securepassword");
    PaymentMethod creditCardPayment = new CreditCard("1234-5678-9012-3456", "123", "123 Main St");
    PaymentMethod bitcoinPayment = new Bitcoin("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa");

    checkout(paypalPayment, 50.00);  
    checkout(creditCardPayment, 100.00);  
    checkout(bitcoinPayment, 200.00);  
}
```

### **Expected Console Output:**
```
Processing PayPal payment of $50.0 for user@example.com
Payment successful!
Processing Credit Card payment of $100.0 for card 1234-5678-9012-3456
Payment successful!
Processing Bitcoin payment of $200.0 to wallet 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
Payment successful!
```

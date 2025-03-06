# Whiteboarding Question: Payment Processing System  

You are designing a payment processing system for an online store. The store supports multiple payment methods.

### **Requirements:**  
1. The checkout system must be able to process any payment in the same way.  
2. Each payment method must have a `process(double amount) -> boolean` function that:  
   - Takes an amount as input.  
   - Returns whether the payment was successful.  
3. Different payment methods require different data to be created:  
   - **PayPal** needs an email and password.  
   - **Credit Card** needs a card number, CVV, and billing address.  
   - **Bitcoin** needs a wallet address.  
4. The system should be easily extendable to support future payment methods.  

### **Task**  
Design and implement the classes required to make this example work. Your solution should:  
- Define a structure that ensures all payment methods can be handled the same way at checkout.  
- Ensure all payment methods follow a consistent structure.  
- Make it easy to add new payment methods without modifying existing code.  

### **Example Expected Usage:**  
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

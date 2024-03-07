[pizza-node-demo/views at starter · kellerflint/pizza-node-demo (github.com)](https://github.com/kellerflint/pizza-node-demo/tree/starter/views)

```js
// Parse URL-encoded bodies (as sent by HTML forms)  
app.use(express.urlencoded({ extended: true }));
```

```js
// Passing order details to the view
res.render('confirmation', { order: orderDetails });
```

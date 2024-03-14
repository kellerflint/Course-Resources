import React from 'react';

const ContentBlock = ({ title, description }) => {
    return (
        <div className="content-block">
            <div className="content-header">
                <span className="content-title">Title: {title}</span>
            </div>
            <p className="content-description">Description: {description}</p>
        </div>
    );
};

const ProductDescription = ({ title, description }) => {
    return (
        <div>
            <h3>Product Description</h3>
            <ContentBlock title={title} description={description} />
        </div>
    );
};

const App = () => {
    const products = [
        { id: 1, title: 'React Book', description: 'Learn React from scratch with this comprehensive guide.' },
        { id: 2, title: 'JavaScript Cookbook', description: 'Solve common problems in web development with this collection of JavaScript tips and tricks.' },
        { id: 3, title: 'CSS Secrets', description: 'Improve your web designs with this collection of CSS techniques.' },
    ];

    return (
        <div>
            <h1>Latest Features</h1>
            <ContentBlock title={products[0].title} description={products[0].description} />

            <h1>Product Catalog</h1>
            {products.map(product => (
                <ProductDescription key={product.id} title={product.title} description={product.description} />
            ))}
        </div>
    );
};

export default App;
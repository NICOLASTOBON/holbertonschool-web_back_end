/* eslint-disable */

const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const client = redis.createClient();

const PORT = 1245;

// mock products
const listProducts = [
  {
    itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4,
  },
  {
    itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10,
  },
  {
    itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2,
  },
  {
    itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5,
  },
];

// transform get and set fuctions redis to promise
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

// function that list all products
const getItemById = (id) => listProducts.filter((product) => product.itemId === id);

// reserve functions
const reserveStockById = (itemId, stock) => setAsync(`item.${itemId}`, stock);
const getCurrentReservedStockById = async (itemId) => getAsync(`item.${itemId}`);

// Endpoints
app.get('/list_products', (req, res) => res.send(listProducts));

app.get('/list_products/:itemId', async (req, res) => {
  const id = req.params.itemId;
  const product = getItemById(parseInt(id))[0];

  if (!product) return res.send({ "status":"Product not found" });

  const currentStock = await getCurrentReservedStockById(id);
  if (!currentStock) {
    await reserveStockById(id, product.initialAvailableQuantity);
    product.currentQuantity = product.initialAvailableQuantity;
  } else {
    product.currentQuantity = parseInt(currentStock);
  }

  res.send(product);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const id = req.params.itemId;
  const product = getItemById(parseInt(id))[0];

  if (!product) return res.send({ "status":"Product not found" });

  const currentStock = await getCurrentReservedStockById(id);
  if (!currentStock) {
    await reserveStockById(id, product.initialAvailableQuantity - 1);
    res.send({ "status":"Reservation confirmed","itemId": id });
  } else if (currentStock > 0) {
    await reserveStockById(id, currentStock - 1);
    res.send({ "status":"Reservation confirmed","itemId": id });
  } else {
    res.send({ "status":"Not enough stock available","itemId": id });
  }
});

// Server
app.listen(PORT, () => console.log(`app listening at http://localhost:${PORT}`));

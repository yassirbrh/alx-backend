#!/usr/bin/node


import { promisify } from 'util';
import { createClient } from 'redis';
import express from 'express';

const listProducts = [
  {
    Id: 1, name: 'Suitcase 250', price: 50, stock: 4,
  },
  {
    Id: 2, name: 'Suitcase 450', price: 100, stock: 10,
  },
  {
    Id: 3, name: 'Suitcase 650', price: 350, stock: 2,
  },
  {
    Id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
  },
];

function transform(product) {
  const modified = {};
  modified.itemId = product.Id;
  modified.itemName = product.name;
  modified.price = product.price;
  modified.initialAvailableQuantity = product.stock;
  return modified;
}

function getItemById(id) {
  for (const product of listProducts) {
    if (product.Id === id) {
      return transform(product);
    }
  }
  return {};
}

function getItems() {
  return listProducts.map(transform);
}

function reserveStockById(itemId, stock) {
  const SET = promisify(redisClient.SET).bind(redisClient);
  return SET(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const GET = promisify(redisClient.GET).bind(redisClient);
  const stock = await GET(`item.${itemId}`);
  if (stock === null) return 0;
  return stock;
}

const redisClient = createClient();
const port = 1245;

redisClient.on('err', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const app = express();

app.get('/list_products', (req, resp) => {
  resp.json(getItems());
});

app.get('/list_products/:itemId', async (req, resp) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (Object.values(item).length > 0) {
    const stock = await getCurrentReservedStockById(itemId);
    item.currentQuantity = item.initialAvailableQuantity - stock;
    return resp.json(item);
  }
  return resp.json({ status: 'Product not found' });
});

app.get('/reserve_product/:itemId', async (req, resp) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (Object.values(item).length === 0) {
    return resp.json({ status: 'Product not found' });
  }
  const stock = await getCurrentReservedStockById(itemId);
  if (stock >= item.initialAvailableQuantity) {
    return resp.json({ status: 'Not enough stock available', itemId });
  }
  await reserveStockById(itemId, Number(stock) + 1);
  return resp.json({ status: 'Reservation confirmed', itemId });
});

function clearRedisStock() {
  const SET = promisify(redisClient.SET).bind(redisClient);
  return Promise.all(listProducts.map((item) => SET(`item.${item.Id}`, 0)));
}

app.listen(port, async () => {
  await clearRedisStock();
  console.log(`API available on localhost via port ${port}`);
});
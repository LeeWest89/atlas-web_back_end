// function to check item stock

const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

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
const app = express();
const port = 1245;
const client = redis.createClient();
const getA = promisify(client.get).bind(client);

function getItemById(id) {
  return (listProducts.find((product) => product.itemId === id));
}

function reserveStockById(itemId, stock) {
  client.set(`itemId.${itemId}`, stock.toString());
}

async function getCurrentReservedStockById(itemId) {
  const reserved = await getA(`itemId.${itemId}`);
  return (parseInt(reserved, 10) || 0);
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);
  const initialQuantity = item ? item.initialAvailableQuantity : 0;
  const currentQuantity = await getCurrentReservedStockById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const info = {
    ...item,
    currentQuantity: initialQuantity - currentQuantity,
  };

  res.json(info);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);
  const initialQuantity = item ? item.initialAvailableQuantity : 0;
  const currentQuantity = await getCurrentReservedStockById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  if (currentQuantity >= initialQuantity) {
    res.json({ status: 'Not enough stock available', itemId });
  } else {
    reserveStockById(itemId, currentQuantity + 1);
    res.json({ status: 'Reservation confirmed', itemId });
  }
});

app.listen(port, () => {});

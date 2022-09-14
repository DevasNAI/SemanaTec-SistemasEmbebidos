var express = require('express');
var app = express();
//  El server no tiene memoria.
app.use(express.json());



var listaTemp = [
    {temperature:"value", time:"time-stamp", stable: "stability"}
];

//	Invoco la funcion get y busco el root con el req a la dirección base.
//  Definimos root
app.get('/', (req, res) => {
	res.send('Conexión exitosa: Datos de Clínica A405');
});

//  Muestra la temperatura
//  GET
app.get('/updated-temperature', (req, res) => {
    const valor = listaTemp.find(c => c.stable === parseInt(req.params.stable));
    if (!valor) res.status(404).send('Not found');
    res.json(valor);
});



/**
 * Delete Game
 * DELETE
 * Para usar este método vamos a usar postmap
 */
 app.delete('/api/games/:id', (req, res) => {
    const valor = listaTemp.find(c => c.stable === parseInt(req.params.stable));
    if( !game) res.status(404).send('Not found');
    var index = games.indexOf(game); 
    //  Borra el id del código
    games.splice(index, 1);
    res.json(game);
});

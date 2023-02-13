const path = require("path")
const express = require("express")
const hbs = require("hbs")
const livereload = require("livereload");
const connectLiveReload = require("connect-livereload");
const { MongoClient } = require('mongodb');

// Connection URL
const dbUrl = "mongodb://0.0.0.0:27017";
const dbClient = new MongoClient(dbUrl);

// Database Name
const dbName = "semalynxDB";

// Create Livereload server and listen to connection events
const liveReloadServer = livereload.createServer();
liveReloadServer.server.once("connection", () => {
	setTimeout(() => {
		liveReloadServer.refresh("/");
	}, 100);
});

const app = express()

app.use(connectLiveReload());

// Define paths for Express config
const publicDirectoryPath = path.join(__dirname, "../public")
const viewsPath = path.join(__dirname, '../templates/views')
const partialsPath = path.join(__dirname, "../templates/partials")

// Setup handlebars engine and directories
app.set("view engine", "hbs")
app.set('views', viewsPath);
app.use(express.static(publicDirectoryPath))
hbs.registerPartials(partialsPath)

const semaboxes = {
	0: {
		name: "Semabox 0",
		version: "1.9.12",
		ip: "198.168.18.2",
		publicIp: "123.45.67.89",
		dns: "ceci est un dns",
		state: "connected",
		stateDescription: "Connectée",
		lastSpeedTest: "18,2kb/s",
		connectedMachines: [
			{
				name: "connected1",
				ip: "127.0.0.1"
			},
			{
				name: "connected2",
				ip: "127.0.0.1"
			},
			{
				name: "connected3",
				ip: "127.0.0.1"
			},
		]
	},
	1: {
		name: "Semabox 1",
		version: "1.9.12",
	},
	2: {
		name: "Semabox 2",
		version: "1.9.12",
	},
	3: {
		name: "Semabox 3",
		version: "1.8.3",
	},
	4: {
		name: "Semabox 4",
		version: "1.9.12",
	},
	5: {
		name: "Semabox 5",
		version: "1.8.4",
	},
}

app.get("", (req, res) => {
	res.render("index", {
		semaboxes: semaboxes,
	})
})

app.get("/box/:boxId/details/", (req, res) => {
	let boxDetails = semaboxes[req.params["boxId"]];

	res.render("details", {
		box: boxDetails,
	})
})

// Delete semabox
app.get("/box/:boxId/delete", (req, res) => {
	delete semaboxes[req.params["boxId"]]
	res.redirect('/');
})

// 404 handler
app.get("*", (req, res) => {
	res.render("404", {
		errorMessage: "Page not found. Nothing to see here.",
	})
})

app.listen(3000, () => {
	console.log("Server up on port 3000...")
})
async function getSema(){
	console.log("getSema()");
	const db = dbClient.db(dbName);
	const collection = db.collection('Semabox');
	const semaboxes_tmp = collection.find({"version" : "1.9.12"});
	console.log(semaboxes_tmp);
	await semaboxes_tmp.forEach(doc => console.log(doc));

	//* REQUEST mongoDB
	// const db = dbClient.db(dbName);
	// const collection = db.collection('Semabox');
	// const semaboxes = db.collection('Semabox').find();
	// await semaboxes.forEach(doc => console.log(doc));

	//* INSERT mongoDB
	// let boxDetails = {
	//	 name: "Semabox sisi tavu",
	//	 ip: "198.168.18.2",
	// 	version: "1.9.12",
	//	 publicIp: "123.45.67.89",
	//	 dns: "ceci est un dns",
	//	 state: "connected",
	//	 stateDescription: "Connectée",
	//	 lastSpeedTest: "18,2kb/s",
	//	 connectedMachines: [
	//		 {
	//			 name: "connected1",
	//			 ip: "127.0.0.1"
	//		 },
	//		 {
	//			 name: "connected2",
	//			 ip: "127.0.0.1"
	//		 },
	//		 {
	//			 name: "connected3",
	//			 ip: "127.0.0.1"
	//		 },
	//	 ]
	// }
	// const insertResult = await collection.insertOne(boxDetails);
	// console.log('Inserted documents =>', insertResult);
}
async function main() {
	// Use connect method to connect to the server
	await dbClient.connect();
	console.log('Connected successfully to server');

	return 'done.';
}

function startStop(id){
	console.log('startstop :'+id);
}

main()
	.then(console.log)
	.catch(console.error)
	.finally(() => dbClient.close());


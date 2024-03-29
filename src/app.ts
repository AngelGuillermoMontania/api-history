import express, { Response, Request, NextFunction } from "express";
import morgan from "morgan";
import helmet from "helmet";
import cors from "cors";

// import indexRouter from "./routes/indexRouter.js";
// import productRouter from "./routes/productRouter.js";

const server = express();

// Middlewares
server.use(express.urlencoded({ extended: true }));
server.use(express.json({ limit: "50mb" }));
server.use(morgan("dev")); // messages by console
server.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*"); // update to match the domain you will make the request from
  res.header("Access-Control-Allow-Credentials", "true");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  res.header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE");
  next();
});
server.use(helmet());
server.use(cors());

// Routes
server.use("/", (req, res) => res.send("Welcome to the API!"));
// server.use("/product", productRouter);

interface Error {
  status?: number;
  message?: string;
}

// Error catching endware.
server.use((err: Error, req: Request, res: Response, next: NextFunction) => {
  const status = err.status || 500;
  const message = err.message || err;
  console.error(err);
  res.status(status).send(message);
});

export default server;

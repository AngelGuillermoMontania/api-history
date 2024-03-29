import dotenv from "dotenv";
dotenv.config();
const PORT = process.env.PORT || 3001;

import server from "./src/app";

server.listen(PORT, () => {
  console.log(`SERVER LISTENING IN PORT ${PORT}`); // eslint-disable-line no-console
});

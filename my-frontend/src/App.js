import React, { useEffect, useState } from "react";
import { getData } from "./services/api";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    getData().then((res) => setData(res));
  }, []);

  return (
    <div>
      <h1>My Chatbot Frontend</h1>
      {data ? <p>Data: {JSON.stringify(data)}</p> : <p>Loading...</p>}
    </div>
  );
}

export default App;

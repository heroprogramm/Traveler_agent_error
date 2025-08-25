import { useUser, useAuth } from "@clerk/nextjs";

const { getToken } = useAuth();

async function sendQueryToBackend(query) {
  try {
    const token = await getToken({ template: "your-template" }); // Clerk JWT
    const res = await fetch("http://localhost:8000/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`, // send JWT
      },
      body: JSON.stringify({ query }),
    });

    const data = await res.json();
    console.log("AI Response:", data);
  } catch (err) {
    console.error("Error sending query:", err);
  }
}

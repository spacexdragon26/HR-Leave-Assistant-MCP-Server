🧾 HR Leave Assistant MCP Server

An MCP (Model Context Protocol) server that automates and streamlines HR leave management. It enables AI tools like Claude Desktop to handle leave requests, approvals, and balance tracking through simple tool-based interactions.

🚀 Features
Submit leave requests through MCP tools
Approve or reject leave requests (HR/admin flow)
Track employee leave balances
Fetch leave history per user
Easy integration with AI assistants (Claude Desktop / MCP clients)
Lightweight Python-based backend

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/spacexdragon26/HR-Leave-Assistant-MCP-Server.git
cd HR-Leave-Assistant-MCP-Server

2. Create a virtual environment (recommended)
python -m venv venv

Activate it:

Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate


3. Install dependencies

If you're using pyproject.toml:

pip install .

Or if you use a requirements file:

pip install -r requirements.txt


4. Run the MCP server with uv
uv run main.py


🔌 Connecting with Claude Desktop (or MCP Client)
Open Claude Desktop settings
Add MCP server configuration
Point it to your local server entry file (main.py)
Restart Claude Desktop
Tools should now appear automatically

⚠️ Common Issues

❌ MCP tools not showing up
Ensure server is running before launching Claude Desktop
Check MCP config path
Restart Claude after changes

❌ ModuleNotFoundError
Activate virtual environment
Reinstall dependencies

❌ Server not responding
Check port conflicts
Ensure main.py is entry point

🛠 Tech Stack
Python
MCP (Model Context Protocol)
uv package manager
FastAPI / Custom tool layer (if used internally)
Claude Desktop integration

📌 Future Improvements
Database persistence (PostgreSQL / SQLite)
Docker support for easy deployment

⚠️ Compatibility Notes
🐍 Python Version Issue (Important)

This project may not work correctly with Python 3.14 due to compatibility issues with some dependencies and MCP-related tooling.

If you encounter unexpected errors during installation or runtime (such as module import failures or tool initialization issues), it is recommended to use:

✅ Python 3.10 – 3.12 (Recommended)

Thankyou!
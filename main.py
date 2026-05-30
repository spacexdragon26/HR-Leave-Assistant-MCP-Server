from typing import Dict, List
from mcp.server.fastmcp import FastMCP
from datetime import datetime, timedelta

mcp = FastMCP("HR-Leave-Assistant")

# Mock database


employees = {
    101: {
        "name": "Alice Johnson",
        "department": "Engineering",
        "leave_balance": 12,

        # Leave history directly inside employee record
        "leave_history": []
    },

    102: {
        "name": "Bob Smith",
        "department": "HR",
        "leave_balance": 8,

        # Leave history directly inside employee record
        "leave_history": []
    },
}

leave_requests: List[Dict] = []

@mcp.tool()
def apply_leave(
    empid : int,
    start_date : str,
    end_date : str,
    reason : str
) -> Dict:

    """ Employee applies for leave """
    
    if empid not in employees:
        return {"error": "Employee not found"}

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")


    leave_days = (end - start).days + 1


    if leave_days <= 0:
        return {"error": "Invalid leave dates"}
    
    if employees[empid]["leave_balance"] < leave_days:
        return {
            "error": "Insufficient leave balance",
            "available_balance": employees[empid]["leave_balance"],
        }

    request = {
        "request_id": len(leave_requests) + 1,
        "employee_id": empid,
        "employee_name": employees[empid]["name"],
        "start_date": start_date,
        "end_date": end_date,
        "days": leave_days,
        "reason": reason,
        "status": "Pending"
        
    }

    leave_requests.append(request)

    current_date = start

    while current_date <= end:

        employees[empid]["leave_history"].append(
        current_date.strftime("%Y-%m-%d")
    )

        current_date += timedelta(days=1)
    
    return {
        "message": "Leave request submitted successfully",
        "request": request,
    }


@mcp.tool()
def approve_leave(request_id: int) -> Dict:

    for request in leave_requests:

        if request["request_id"] == request_id:

            if request["status"] != "Pending":
                return {
                    "error": f"Your leave request is already {request['status']}"
                }

            employee_id = request["employee_id"]
            leave_days = request["days"]

            employees[employee_id]["leave_balance"] -= leave_days

            request["status"] = "Approved"

            employees[employee_id]["leave_history"].append({
                "start_date": request["start_date"],
                "end_date": request["end_date"]
            })

            return {
                "message": "Leave has been approved successfully",
                "updated_balance": employees[employee_id]["leave_balance"],
                "request": request
            }

    return {
        "error": "Leave request not found!"
    }


@mcp.tool()
def reject_leave(request_id : int) -> Dict :

    for request in leave_requests:
        if(request["request_id"] == request_id):

            if(request["status"] != "Pending"):
                return{
                    "error" : f"Your leave request is already {request['status']}"
                      }
            
            employee_id = request["employee_id"]
            leave_days = request["days"]
            leave_balance = employees[employee_id]["leave_balance"]

            if(request["days"] > employees[employee_id]["leave_balance"]):
                request["status"] = "Rejected"
                return{
                    "error": "Leave request rejected as number of days requested are more than leave balance",
                    "request": request
      
                }
            
    return{
        "error": "Request not found"
    }    

@mcp.tool()
def get_leave_balance(employee_id: int) -> int:

    if employee_id not in employees:
        return {"error": "Employee not found"}

    employee = employees[employee_id]


    leave_balance = employee["leave_balance"]

    return{
        "message": f"{employee['name']} has {leave_balance} left"
    }

###resources

@mcp.resource("greeting://{name}") 
def get_greeting(name: str) -> str :
    return f"Hii {name}!, how can I help you today?"
    


@mcp.resource("employee://{empid}")
def employee_details(empid: str) -> Dict:
    """
    Fetch employee details
    """

    employee_id = int(empid)

    if employee_id not in employees:
        return {"error": "Employee not found"}

    return employees[employee_id]



if __name__ == "__main__":
    mcp.run()


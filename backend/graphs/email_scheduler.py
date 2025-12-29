import schedule
import time
from backend.graphs.email_graph_flow import run_email_flow

def start_scheduler():
    print("Scheduler started...")
    schedule.every(10).seconds.do(run_email_flow)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped. Exiting clean.")
        exit(0)

if __name__ == "__main__":
    start_scheduler()
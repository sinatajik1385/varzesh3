import threading
import subprocess
import time
def do_stuff () :
    def run_script(script_name):
        subprocess.run(["python", script_name])

    if __name__ == "__main__":
        script1_thread = threading.Thread(target=run_script, args=(r"web_scrape\leagues.py",))
        script2_thread = threading.Thread(target=run_script, args=(r"web_scrape\news_videos.py",))




        script1_thread.start()
        script2_thread.start()


        script1_thread.join()
        script2_thread.join()

        a = "all scripts have finished executing."

        print("all scripts have finished executing.")
        time_wait = 30
        print (f'waiting {time_wait} minuts')
        time.sleep (time_wait *60)
        
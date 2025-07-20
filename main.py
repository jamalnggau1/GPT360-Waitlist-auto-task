import requests

url_base = "https://launchpad-api.arenavs.com"

list_task = [
    "8783a6ae-f766-464b-9497-f39e09e36335",
    "4a20f1ce-b554-4cbb-b28b-61d409dd2985",
    "0bc685b5-c3ca-44bc-8b2f-af07e2fc031e",
    "da24ffb5-c296-4470-b640-2b76a9db5c65",
    "d8e94d87-a7e4-4b5f-b0e1-5e38a9e3c121",
    "2488fcb9-a987-4bf5-a385-cdb8f7a7cba1",
    "134278f1-465d-4bcd-b34f-4e37d2f9618d",
    "68b319d1-e707-4bbe-9d2d-dfeffd52b3bf",
    "3d131806-2eed-4630-8fe4-ff3b1cd2b882",
]

def complete_task(task_id, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    url = f"{url_base}/api/v1/tasks/{task_id}/complete"
    try:
        response = requests.post(url, headers=headers)
        data = response.json()
        if response.status_code == 200:
            print(f"✅ [{auth_token[:10]}...] Task {task_id} completed successfully.")
        elif response.status_code == 400 and data.get("message") == "Task already completed":
            print(f"⚠️  [{auth_token[:10]}...] Task {task_id} already completed.")
        else:
            message = data.get("message")
            task_name = data.get("taskName") or data.get("task_name")
            if message:
                print(f"❌ [{auth_token[:10]}...] Task {task_id} failed: {message}")
            elif task_name:
                print(f"❌ [{auth_token[:10]}...] Gagal menyelesaikan task: {task_name}")
            else:
                print(f"❌ [{auth_token[:10]}...] Task {task_id} gagal diselesaikan (tidak ada pesan).")
    except Exception as e:
        print(f"❌ Error dengan token [{auth_token[:10]}...]: {e}")

try:
    with open("wallets.txt", "r") as f:
        all_tokens = [line.strip() for line in f if line.strip()]

    for token in all_tokens:
        print(f"\n🔑 Menggunakan akun: {token[:10]}...")
        for task_id in list_task:
            complete_task(task_id, token)

except KeyboardInterrupt:
    print("\n🛑 Dihentikan oleh pengguna (Ctrl + C). Program keluar dengan aman.")

def main():
    tasks = []
    print("--- Sumeet's Task Manager ---")
    
    while True:
        choice = input("\n1. Tasks: ")
        
        if choice == '1':
            t = input("Enter task: ")
            tasks.append(t)
        elif choice == '2':
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        elif choice == '3':
            break

if __name__ == "__main__":
    main()

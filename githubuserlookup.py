import requests

def get_github_profile(username):
    # GitHub REST API endpoint for users
    url = f"https://github.com{username}"
    
    try:
        response = requests.get(url)
        
        # Implementation Guideline: Check HTTP status code
        if response.status_code == 404:
            print(f"\n❌ Error: Username '{username}' not found. Please try again.")
            return None
        elif response.status_code != 200:
            print(f"\n❌ Error: Unable to fetch data (Status Code: {response.status_code})")
            return None
            
        # Parse JSON data
        data = response.json()
        
        # Implementation Guideline: Print raw JSON during testing if needed
        # print(data) 
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Network error occurred: {e}")
        return None

def get_top_repositories(username):
    # Endpoint to fetch user repositories sorted by recent updates
    url = f"https://github.com{username}/repos?per_page=100"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        pass
    return []

def display_profile(data):
    if not data:
        return

    print("\n" + "="*40)
    print(f"       GITHUB USER PROFILE: {data.get('login')}")
    print("="*40)
    
    # LEVEL 01: MVP Features
    print(f"Name:         {data.get('name', 'N/A')}")
    print(f"Followers:    {data.get('followers', 0)}")
    print(f"Public Repos: {data.get('public_gists', 0) + data.get('public_repos', 0)}")
    
    # LEVEL 02: Extended Details
    print(f"Bio:          {data.get('bio', 'No bio provided')}")
    print(f"Location:     {data.get('location', 'Not specified')}")
    print(f"Company:      {data.get('company', 'Not specified')}")
    print("-"*40)

    # LEVEL 03: Challenge (Fetch and sort top repositories)
    username = data.get('login')
    repos = get_top_repositories(username)
    
    if repos:
        # Sort repositories by stargazers count in descending order
        sorted_repos = sorted(repos, key=lambda x: x.get('stargazers_count', 0), reverse=True)
        
        print("Top Repositories (Sorted by Stars):")
        for i, repo in enumerate(sorted_repos[:5], 1):  # Display top 5
            stars = repo.get('stargazers_count', 0)
            print(f" {i}. {repo.get('name')} (⭐ {stars})")
    else:
        print("No repositories found or unable to load.")
    print("="*40)

def main():
    # Core Feature: Ask for a GitHub username
    print("--- GitHub User Lookup Tool ---")
    username = input("Enter GitHub username: ").strip()
    
    if not username:
        print("Username cannot be empty!")
        return
        
    # Fetch profile data safely
    profile_data = get_github_profile(username)
    
    # Display the structured results
    display_profile(profile_data)

if __name__ == "__main__":
    main()
# Deploying to Render (Free Tier)

Your application is now configured for deployment! Follow these steps to get it online for free using Render.

## 1. Commit Your Changes
First, save all the changes we just made to your GitHub repository.

```bash
git add .
git commit -m "Prepare for Render deployment"
git push
```

## 2. Create a Render Account
1.  Go to [dashboard.render.com](https://dashboard.render.com/).
2.  Sign up/Log in using your **GitHub** account.

## 3. Create a New Web Service
1.  Click the **"New +"** button and select **"Web Service"**.
2.  Select **"Build and deploy from a Git repository"**.
3.  Find your repository in the list and click **"Connect"**.

## 4. Configure the Service
Fill in the following details (most should be auto-detected):

*   **Name**: Choose a name for your app (e.g., `my-portfolio-chat`).
*   **Region**: Choose the one closest to you (e.g., `Singapore`).
*   **Branch**: `main` (or `master`).
*   **Runtime**: `Python 3`.
*   **Build Command**: `pip install -r requirements.txt` (Default is usually correct).
*   **Start Command**: `gunicorn app:app` (This is crucial! It tells Render to use the production server).
*   **Instance Type**: Select **Free**.

## 5. Add Environment Variables
This is the most important step for security.

1.  Scroll down to the **"Environment Variables"** section.
2.  Click **"Add Environment Variable"**.
3.  **Key**: `OPENROUTER_API_KEY`
4.  **Value**: `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` (Copy this exactly).
5.  Click **"Add Environment Variable"** again.
6.  **Key**: `PYTHON_VERSION`
7.  **Value**: `3.11.9` (Or your local version, `3.11.9` is a safe bet).

## 6. Deploy
1.  Click **"Create Web Service"**.
2.  Render will start building your app. This might take a few minutes.
3.  Watch the logs. Once it says **"Live"**, your app is online!
4.  Click the URL at the top (e.g., `https://my-portfolio-chat.onrender.com`) to visit your site.

---

## Troubleshooting
*   **"Build Failed"**: Check the logs. Usually, it's a missing dependency in `requirements.txt`.
*   **"Application Error"**: Check the logs (click "Logs" tab). It might be a missing environment variable or a typo in the Start Command.

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Matan's Blog — README</title>
  <link href="https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,400&family=Sora:wght@300;400;600;700;800&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg: #0d0f14;
      --bg2: #13161e;
      --bg3: #1a1e28;
      --border: #2a2f3d;
      --accent: #e8624a;
      --accent2: #f0a070;
      --text: #e8eaf0;
      --muted: #7a8099;
      --code-bg: #0a0c10;
      --green: #4ade80;
      --blue: #60a5fa;
      --yellow: #fbbf24;
    }

    html { scroll-behavior: smooth; }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Sora', sans-serif;
      font-size: 15px;
      line-height: 1.7;
      min-height: 100vh;
    }

    /* ── HERO ── */
    .hero {
      position: relative;
      padding: 80px 40px 60px;
      text-align: center;
      overflow: hidden;
      border-bottom: 1px solid var(--border);
    }

    .hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 60% 50% at 50% 0%, rgba(232,98,74,.18) 0%, transparent 70%),
        radial-gradient(ellipse 40% 30% at 80% 80%, rgba(96,165,250,.08) 0%, transparent 60%);
      pointer-events: none;
    }

    .hero-badge {
      display: inline-block;
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      letter-spacing: .12em;
      text-transform: uppercase;
      color: var(--accent);
      border: 1px solid rgba(232,98,74,.3);
      border-radius: 99px;
      padding: 4px 14px;
      margin-bottom: 20px;
      animation: fadeUp .5s ease both;
    }

    .hero h1 {
      font-size: clamp(2rem, 5vw, 3.5rem);
      font-weight: 800;
      letter-spacing: -.03em;
      line-height: 1.1;
      animation: fadeUp .6s .1s ease both;
    }

    .hero h1 span { color: var(--accent); }

    .hero p {
      margin-top: 16px;
      color: var(--muted);
      max-width: 560px;
      margin-left: auto;
      margin-right: auto;
      font-weight: 300;
      animation: fadeUp .6s .2s ease both;
    }

    .hero-tags {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      justify-content: center;
      margin-top: 28px;
      animation: fadeUp .6s .3s ease both;
    }

    .tag {
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      padding: 4px 12px;
      border-radius: 6px;
      background: var(--bg3);
      border: 1px solid var(--border);
      color: var(--muted);
    }

    .tag.python { border-color: rgba(96,165,250,.4); color: var(--blue); }
    .tag.flask  { border-color: rgba(74,222,128,.4); color: var(--green); }
    .tag.sql    { border-color: rgba(251,191,36,.4); color: var(--yellow); }
    .tag.auth   { border-color: rgba(232,98,74,.4);  color: var(--accent2); }

    /* ── LAYOUT ── */
    .container {
      max-width: 960px;
      margin: 0 auto;
      padding: 0 24px;
    }

    .grid2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }

    @media (max-width: 640px) { .grid2 { grid-template-columns: 1fr; } }

    /* ── SECTIONS ── */
    section { padding: 56px 0; border-bottom: 1px solid var(--border); }
    section:last-child { border-bottom: none; }

    .section-label {
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      letter-spacing: .14em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 10px;
    }

    h2 {
      font-size: 1.6rem;
      font-weight: 700;
      letter-spacing: -.02em;
      margin-bottom: 28px;
    }

    h3 {
      font-size: 1rem;
      font-weight: 600;
      margin-bottom: 10px;
    }

    /* ── FEATURE CARDS ── */
    .card {
      background: var(--bg2);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 22px 24px;
      transition: border-color .2s, transform .2s;
    }

    .card:hover {
      border-color: rgba(232,98,74,.4);
      transform: translateY(-2px);
    }

    .card-icon {
      font-size: 22px;
      margin-bottom: 10px;
    }

    .card p {
      color: var(--muted);
      font-size: 13.5px;
      line-height: 1.6;
    }

    /* ── TECH STACK ── */
    .stack-row {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 14px 0;
      border-bottom: 1px solid var(--border);
    }

    .stack-row:last-child { border-bottom: none; }

    .stack-label {
      font-family: 'DM Mono', monospace;
      font-size: 12px;
      color: var(--muted);
      width: 100px;
      flex-shrink: 0;
    }

    .stack-value {
      font-size: 13.5px;
      color: var(--text);
    }

    .dot {
      width: 8px; height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }
    .dot-python { background: var(--blue); }
    .dot-flask  { background: var(--green); }
    .dot-sql    { background: var(--yellow); }
    .dot-auth   { background: var(--accent); }
    .dot-ui     { background: #c084fc; }
    .dot-email  { background: var(--accent2); }

    /* ── CODE BLOCK ── */
    .code-block {
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      margin: 20px 0;
    }

    .code-bar {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 10px 16px;
      border-bottom: 1px solid var(--border);
      background: var(--bg3);
    }

    .code-dot { width: 10px; height: 10px; border-radius: 50%; }
    .code-dot:nth-child(1) { background: #ff5f57; }
    .code-dot:nth-child(2) { background: #febc2e; }
    .code-dot:nth-child(3) { background: #28c840; }

    .code-filename {
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      color: var(--muted);
      margin-left: 8px;
    }

    pre {
      font-family: 'DM Mono', monospace;
      font-size: 12.5px;
      line-height: 1.8;
      padding: 20px 24px;
      overflow-x: auto;
      color: #a8b5cc;
    }

    pre .path { color: var(--accent2); }
    pre .comment { color: #4a5568; }

    /* ── ROUTES TABLE ── */
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
    }

    thead tr {
      border-bottom: 2px solid var(--border);
    }

    th {
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      letter-spacing: .08em;
      text-transform: uppercase;
      color: var(--muted);
      padding: 10px 14px;
      text-align: left;
    }

    td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
      color: var(--text);
    }

    tr:hover td { background: var(--bg3); }

    .method {
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 4px;
      font-weight: 500;
    }

    .get  { background: rgba(74,222,128,.12); color: var(--green); border: 1px solid rgba(74,222,128,.25); }
    .post { background: rgba(96,165,250,.12); color: var(--blue);  border: 1px solid rgba(96,165,250,.25); }
    .both { background: rgba(251,191,36,.12); color: var(--yellow); border: 1px solid rgba(251,191,36,.25); }

    .auth-badge {
      font-family: 'DM Mono', monospace;
      font-size: 10px;
      padding: 2px 8px;
      border-radius: 4px;
      background: rgba(232,98,74,.12);
      color: var(--accent);
      border: 1px solid rgba(232,98,74,.25);
    }

    /* ── SETUP STEPS ── */
    .step {
      display: flex;
      gap: 20px;
      margin-bottom: 32px;
    }

    .step-num {
      width: 32px; height: 32px;
      border-radius: 50%;
      background: var(--accent);
      color: white;
      font-weight: 700;
      font-size: 13px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .step-content h3 { margin-bottom: 6px; }
    .step-content p  { color: var(--muted); font-size: 14px; }

    /* ── ENV TABLE ── */
    .env-row {
      display: flex;
      align-items: flex-start;
      gap: 16px;
      padding: 14px 0;
      border-bottom: 1px solid var(--border);
    }

    .env-key {
      font-family: 'DM Mono', monospace;
      font-size: 12.5px;
      color: var(--accent2);
      min-width: 160px;
      flex-shrink: 0;
    }

    .env-desc {
      font-size: 13.5px;
      color: var(--muted);
    }

    /* ── FOOTER ── */
    .page-footer {
      text-align: center;
      padding: 40px 24px;
      font-family: 'DM Mono', monospace;
      font-size: 12px;
      color: var(--muted);
      border-top: 1px solid var(--border);
    }

    /* ── ANIMATIONS ── */
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(18px); }
      to   { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-badge">README · Flask Blog · 2024</div>
  <h1>Matan's <span>Blog</span></h1>
  <p>A full-stack blog application built with Flask, featuring user authentication, blog post creation, commenting, and contact form functionality.</p>
  <div class="hero-tags">
    <span class="tag python">Python</span>
    <span class="tag flask">Flask</span>
    <span class="tag sql">SQLAlchemy</span>
    <span class="tag auth">Flask-Login</span>
    <span class="tag">Bootstrap 5</span>
    <span class="tag">CKEditor</span>
    <span class="tag">Gravatar</span>
  </div>
</div>

<div class="container">

  <!-- FEATURES -->
  <section>
    <div class="section-label">01 · Overview</div>
    <h2>Features</h2>
    <div class="grid2">
      <div class="card">
        <div class="card-icon">🔐</div>
        <h3>Authentication</h3>
        <p>User registration and login with Werkzeug-hashed passwords and Flask-Login session management.</p>
      </div>
      <div class="card">
        <div class="card-icon">🛡️</div>
        <h3>Admin Controls</h3>
        <p>Admin-only decorator restricts creating, editing, and deleting posts to user ID 1.</p>
      </div>
      <div class="card">
        <div class="card-icon">✍️</div>
        <h3>Rich Text Editor</h3>
        <p>Blog posts and comments use CKEditor for full rich-text formatting support.</p>
      </div>
      <div class="card">
        <div class="card-icon">💬</div>
        <h3>Comments + Gravatar</h3>
        <p>Logged-in users can comment on posts. Profile images are pulled automatically from Gravatar.</p>
      </div>
      <div class="card">
        <div class="card-icon">📧</div>
        <h3>Contact Form</h3>
        <p>Sends emails via Office365 SMTP with a rate limit of 2 emails per 2-hour window.</p>
      </div>
      <div class="card">
        <div class="card-icon">📱</div>
        <h3>Responsive UI</h3>
        <p>Fully responsive layout using Bootstrap 5, Font Awesome icons, and Google Fonts.</p>
      </div>
    </div>
  </section>

  <!-- TECH STACK -->
  <section>
    <div class="section-label">02 · Stack</div>
    <h2>Tech Stack</h2>
    <div class="stack-row"><span class="dot dot-python"></span><span class="stack-label">Backend</span><span class="stack-value">Python, Flask</span></div>
    <div class="stack-row"><span class="dot dot-sql"></span><span class="stack-label">Database</span><span class="stack-value">SQLite (dev) / configurable via DB_URI env variable</span></div>
    <div class="stack-row"><span class="dot dot-sql"></span><span class="stack-label">ORM</span><span class="stack-value">SQLAlchemy with DeclarativeBase</span></div>
    <div class="stack-row"><span class="dot dot-auth"></span><span class="stack-label">Auth</span><span class="stack-value">Flask-Login + Werkzeug password hashing (pbkdf2:sha256)</span></div>
    <div class="stack-row"><span class="dot dot-flask"></span><span class="stack-label">Forms</span><span class="stack-value">Flask-WTF, WTForms</span></div>
    <div class="stack-row"><span class="dot dot-flask"></span><span class="stack-label">Editor</span><span class="stack-value">Flask-CKEditor</span></div>
    <div class="stack-row"><span class="dot dot-email"></span><span class="stack-label">Email</span><span class="stack-value">smtplib via Office365 SMTP (smtp.office365.com:587)</span></div>
    <div class="stack-row"><span class="dot dot-ui"></span><span class="stack-label">UI</span><span class="stack-value">Bootstrap 5, Font Awesome 6, Google Fonts (Lora + Open Sans)</span></div>
  </section>

  <!-- PROJECT STRUCTURE -->
  <section>
    <div class="section-label">03 · Structure</div>
    <h2>Project Structure</h2>
    <div class="code-block">
      <div class="code-bar">
        <div class="code-dot"></div>
        <div class="code-dot"></div>
        <div class="code-dot"></div>
        <span class="code-filename">project root</span>
      </div>
      <pre><span class="path">├── main.py</span>               <span class="comment"># Flask app, routes, DB models</span>
<span class="path">├── forms.py</span>              <span class="comment"># WTForms definitions</span>
<span class="path">├── .env</span>                  <span class="comment"># Environment variables (not committed)</span>
<span class="path">├── templates/</span>
<span class="path">│   ├── header.html</span>       <span class="comment"># Navbar + head section</span>
<span class="path">│   ├── footer.html</span>       <span class="comment"># Footer + scripts</span>
<span class="path">│   ├── index.html</span>        <span class="comment"># Homepage — lists all posts</span>
<span class="path">│   ├── post.html</span>         <span class="comment"># Individual post + comments</span>
<span class="path">│   ├── make-post.html</span>    <span class="comment"># Create / edit post form</span>
<span class="path">│   ├── register.html</span>     <span class="comment"># User registration</span>
<span class="path">│   ├── login.html</span>        <span class="comment"># User login</span>
<span class="path">│   ├── about.html</span>        <span class="comment"># About page</span>
<span class="path">│   └── contact.html</span>      <span class="comment"># Contact form</span>
<span class="path">└── static/</span>
<span class="path">    ├── css/styles.css</span>    <span class="comment"># Custom styles</span>
<span class="path">    ├── js/scripts.js</span>     <span class="comment"># Custom scripts</span>
<span class="path">    └── assets/</span>           <span class="comment"># Images + favicon</span></pre>
    </div>
  </section>

  <!-- SETUP -->
  <section>
    <div class="section-label">04 · Setup</div>
    <h2>Installation</h2>

    <div class="step">
      <div class="step-num">1</div>
      <div class="step-content">
        <h3>Clone the repository</h3>
        <div class="code-block">
          <div class="code-bar"><div class="code-dot"></div><div class="code-dot"></div><div class="code-dot"></div><span class="code-filename">terminal</span></div>
          <pre>git clone &lt;your-repo-url&gt;
cd your-project-folder</pre>
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-num">2</div>
      <div class="step-content">
        <h3>Create a virtual environment</h3>
        <div class="code-block">
          <div class="code-bar"><div class="code-dot"></div><div class="code-dot"></div><div class="code-dot"></div><span class="code-filename">terminal</span></div>
          <pre>python -m venv venv
source venv/bin/activate      <span class="comment"># Mac/Linux</span>
venv\Scripts\activate         <span class="comment"># Windows</span></pre>
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-num">3</div>
      <div class="step-content">
        <h3>Install dependencies</h3>
        <div class="code-block">
          <div class="code-bar"><div class="code-dot"></div><div class="code-dot"></div><div class="code-dot"></div><span class="code-filename">terminal</span></div>
          <pre>pip install flask flask-wtf flask-login flask-sqlalchemy \
  flask-bootstrap flask-ckeditor flask-gravatar \
  werkzeug python-dotenv</pre>
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-num">4</div>
      <div class="step-content">
        <h3>Create your .env file</h3>
        <div class="code-block">
          <div class="code-bar"><div class="code-dot"></div><div class="code-dot"></div><div class="code-dot"></div><span class="code-filename">.env</span></div>
          <pre>FLASK_KEY=your_secret_key_here
DB_URI=sqlite:///posts.db
EMAIL_KEY=your_email@outlook.com
PASSWORD_KEY=your_email_password</pre>
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-num">5</div>
      <div class="step-content">
        <h3>Run the app</h3>
        <div class="code-block">
          <div class="code-bar"><div class="code-dot"></div><div class="code-dot"></div><div class="code-dot"></div><span class="code-filename">terminal</span></div>
          <pre>python main.py</pre>
        </div>
        <p>Visit <strong>http://localhost:5000</strong> in your browser.</p>
      </div>
    </div>
  </section>

  <!-- ROUTES -->
  <section>
    <div class="section-label">05 · API</div>
    <h2>Routes</h2>
    <table>
      <thead>
        <tr>
          <th>Method</th>
          <th>Route</th>
          <th>Description</th>
          <th>Auth</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><span class="method get">GET</span></td><td><code>/</code></td><td>Homepage — all posts</td><td>—</td></tr>
        <tr><td><span class="method both">GET/POST</span></td><td><code>/register</code></td><td>Register new user</td><td>—</td></tr>
        <tr><td><span class="method both">GET/POST</span></td><td><code>/login</code></td><td>Login</td><td>—</td></tr>
        <tr><td><span class="method get">GET</span></td><td><code>/logout</code></td><td>Logout current user</td><td>—</td></tr>
        <tr><td><span class="method both">GET/POST</span></td><td><code>/new-post</code></td><td>Create new blog post</td><td><span class="auth-badge">Admin only</span></td></tr>
        <tr><td><span class="method both">GET/POST</span></td><td><code>/edit-post/&lt;id&gt;</code></td><td>Edit existing post</td><td><span class="auth-badge">Admin only</span></td></tr>
        <tr><td><span class="method get">GET</span></td><td><code>/delete/&lt;id&gt;</code></td><td>Delete a post</td><td><span class="auth-badge">Admin only</span></td></tr>
        <tr><td><span class="method both">GET/POST</span></td><td><code>/post/&lt;id&gt;</code></td><td>View post + add comment</td><td>Comment: Yes</td></tr>
        <tr><td><span class="method get">GET</span></td><td><code>/about</code></td><td>About page</td><td>—</td></tr>
        <tr><td><span class="method both">GET/POST</span></td><td><code>/contact</code></td><td>Contact form + email send</td><td>—</td></tr>
      </tbody>
    </table>
  </section>

  <!-- ENV VARS -->
  <section>
    <div class="section-label">06 · Config</div>
    <h2>Environment Variables</h2>
    <div class="env-row"><span class="env-key">FLASK_KEY</span><span class="env-desc">Flask secret key used for session signing and CSRF protection</span></div>
    <div class="env-row"><span class="env-key">DB_URI</span><span class="env-desc">Database connection string. Defaults to sqlite:///posts.db if not set</span></div>
    <div class="env-row"><span class="env-key">EMAIL_KEY</span><span class="env-desc">Sender email address used for the contact form (Outlook/Office365)</span></div>
    <div class="env-row"><span class="env-key">PASSWORD_KEY</span><span class="env-desc">Email account password or app-specific password for SMTP auth</span></div>
  </section>

</div>

<div class="page-footer">
  MIT License · Matan's Blog · Built with Flask
</div>

</body>
</html>

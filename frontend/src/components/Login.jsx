import './Login.css'

export default function Login() {
  function handleLogin() {
    window.location.href = '/api/auth/google/login'
  }

  return (
    <div className="login">
      <div className="login-box">
        <div className="login-header">
          <span className="login-label">SYSTEM // TAU CETI FIELD OPS</span>
          <span className="login-status">
            <span className="login-status-dot" /> ACCESS RESTRICTED
          </span>
        </div>

        <h1 className="login-title" data-text="TAU CETI">TAU CETI</h1>
        <p className="login-subtitle">[ RUNNER FIELD TRACKER ]</p>

        <div className="login-divider" />

        <p className="login-prompt">IDENTITY VERIFICATION REQUIRED</p>
        <p className="login-subprompt">Clearance must be confirmed before access is granted.</p>

        <button className="login-btn" onClick={handleLogin}>
          ▶ AUTHENTICATE VIA GOOGLE
        </button>

        <div className="login-footer">
          <span className="cursor-blink">_</span>
        </div>
      </div>
    </div>
  )
}

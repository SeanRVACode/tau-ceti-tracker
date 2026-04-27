import './Header.css'

export default function Header({ authed }) {
  return (
    <header className="header">
      <div className="header-top-bar">
        <span className="header-label">UESC MARATHON SYSTEM // TAU CETI IV FIELD OPS</span>
        <div className="header-top-right">
          {!authed && (
            <a className="header-login-link" href="/api/auth/google/login">
              [ LOGIN ]
            </a>
          )}
          <span className="header-status">
            <span className="status-dot" /> UPLINK ACTIVE
          </span>
        </div>
      </div>

      <div className="header-title-block">
        <div className="header-glitch-wrap">
          <h1 className="header-title" data-text="TAU CETI">TAU CETI</h1>
        </div>
        <h2 className="header-subtitle">[ RUNNER FIELD TRACKER ]</h2>
      </div>

      <div className="header-bottom-bar">
        <span>UESC MARATHON — RUNNER RECORD</span>
        <span className="cursor-blink">_</span>
      </div>
    </header>
  )
}

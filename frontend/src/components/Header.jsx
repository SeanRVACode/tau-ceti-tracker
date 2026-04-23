import './Header.css'

export default function Header() {
  return (
    <header className="header">
      <div className="header-top-bar">
        <span className="header-label">SYSTEM // TAU CETI FIELD OPS</span>
        <span className="header-status">
          <span className="status-dot" /> UPLINK ACTIVE
        </span>
      </div>

      <div className="header-title-block">
        <div className="header-glitch-wrap">
          <h1 className="header-title" data-text="TAU CETI">TAU CETI</h1>
        </div>
        <h2 className="header-subtitle">[ RUNNER FIELD TRACKER ]</h2>
      </div>

      <div className="header-bottom-bar">
        <span>CRYO ARCHIVE — SECTOR 7</span>
        <span className="cursor-blink">_</span>
      </div>
    </header>
  )
}

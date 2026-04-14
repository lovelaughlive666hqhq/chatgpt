# ReachRipple Advertising Platform — UX/Layout & Structure Review

**Review date:** 2026-04-14 (UTC)  
**Target URL:** https://reachripple-live-web.onrender.com/  
**Review mode:** Remote quick audit (limited runtime execution in this environment)

---

## 1) Executive Summary

Your platform should focus on a **clean, conversion-first information hierarchy**:

1. **Above the fold:** clear value proposition + one primary CTA.
2. **Proof section:** outcomes, logos, testimonials.
3. **How-it-works:** 3 simple setup steps.
4. **Plans/pricing:** transparent limits and expected results.
5. **Product preview:** dashboard screenshots and key metrics.

This layout reduces decision friction and improves trial-to-campaign activation.

---

## 2) What Was Verified in This Environment

| Check | Result | Notes |
|---|---|---|
| Basic reachability | ✅ Pass | Site responds and serves HTML shell. |
| App rendering | ⚠️ Partial | HTML indicates JS app bootstrap (`enable JavaScript` message). |
| Full interaction flow | ⚠️ Not executed | Requires real browser JS execution + authenticated user path. |
| CLI network fetch | ❌ Blocked | `curl` failed here with proxy/connect restriction (403 tunnel). |

---

## 3) Recommended Page Layout (High-Impact Redesign)

## A. Landing/Homepage Structure (Top to Bottom)

### Hero (first viewport)
- Headline formula: **Outcome + audience + speed**.
- Subheadline: one sentence on what makes ReachRipple different.
- CTA row: `Start Campaign` (primary) + `See Demo` (secondary).
- Right side visual: campaign builder screenshot or 20–30 sec product loop.

### Trust/Proof strip
- Client logos, campaign counts, managed spend, avg ROAS uplift.
- Keep this directly below hero to reduce skepticism early.

### How it works (3 steps)
- Step 1: Define objective.
- Step 2: Build audience + creatives.
- Step 3: Launch + optimize via insights.
- Use icon cards with concise copy (1 line each).

### Feature grid (problem/solution format)
- Left column: advertiser pain points.
- Right column: ReachRipple feature response.
- Improves message clarity vs feature-only lists.

### Pricing/Plans
- Clear differentiation by usage limits and support level.
- Add "Best for" labels (solo, SMB, agency).
- Keep one highlighted recommended plan.

### Final CTA + FAQ
- Answer objections: integrations, billing, attribution accuracy, onboarding time.
- End with strong CTA and zero-commitment reassurance.

---

## 4) Dashboard Information Architecture (Inside the Product)

### Primary nav (left)
1. Dashboard
2. Campaigns
3. Audiences
4. Creatives
5. Analytics
6. Billing
7. Settings

### Dashboard top row (must be visible immediately)
- Spend (Today / 7d / 30d)
- Impressions
- CTR
- Conversions
- CPA
- ROAS

### Dashboard middle
- Trend charts for spend, CTR, conversions.
- Alerts panel (spend spike, CTR drop, disapproved ads).

### Dashboard bottom
- Top campaigns table with inline actions (pause, duplicate, edit budget).
- Recent activity log (who changed what and when).

This structure helps operators act quickly without hunting through tabs.

---

## 5) Design System & Visual Consistency

### Spacing & grid
- Adopt consistent spacing scale (e.g., 4/8/12/16/24/32).
- Use a max content width and predictable section rhythm.

### Typography
- 1 display style + 2 text sizes for body hierarchy.
- Maintain readable line length (roughly 60–80 chars).

### Components
- Standardize button hierarchy (primary/secondary/tertiary).
- Reuse card patterns for metrics, alerts, and campaign rows.
- Use consistent empty/loading/error states with actionable next step.

### Color and status semantics
- Green = positive trend, Amber = warning, Red = critical.
- Avoid relying on color alone; include icon + label for accessibility.

---

## 6) Mobile Layout Priorities

- Collapse nav into bottom tabs or clear drawer pattern.
- Keep KPI cards horizontally scrollable or stacked with priority order.
- Ensure campaign publish actions are sticky and easy to reach.
- Reduce heavy chart payload on first mobile load.

---

## 7) Performance & Technical UX Priorities

1. Route-level code splitting for dashboard modules.
2. Lazy-load heavy chart libraries.
3. Optimize media assets (WebP/AVIF + responsive sizes).
4. Cache hashed static assets aggressively.
5. Track and alert on Core Web Vitals regressions.

---

## 8) Suggested Validation Plan for Layout/Structure Improvements

### Phase 1 — Fast UX checks (1–2 days)
- Heuristic review against the layout above.
- Mobile breakpoint review (320px, 375px, 768px, 1024px, 1440px).
- Accessibility scan (contrast, heading order, focus states).

### Phase 2 — Behavioral tests (3–5 days)
- Session recordings on signup and first campaign creation.
- Funnel drop-off analysis at each onboarding step.
- A/B test hero + CTA arrangement.

### Phase 3 — Product analytics (ongoing)
- Measure time-to-first-campaign.
- Measure campaign publish success rate.
- Track weekly active advertisers and retention cohorts.

---

## 9) Constraints Encountered During This Review

- This environment could retrieve only initial HTML via fetch tooling.
- Full JS-driven behavior (auth forms, dashboard interactions, billing) was not executable here.
- Direct CLI HTTP request from this environment failed with proxy/connect tunnel restriction.


---

## 10) Page-by-Page Wireframe Blueprint (Build Spec)

## A. Public Marketing Site

### 1. Home (`/`)
1. **Header**: logo, nav (Features, Pricing, Resources), CTA (`Start Campaign`).
2. **Hero**: headline, subheadline, primary/secondary CTA, product visual.
3. **Trust Bar**: logos + proof metrics.
4. **How It Works (3 Cards)**: objective → audience/creative → launch/optimize.
5. **Feature Sections**: pain point left, solution right (alternating layout).
6. **Pricing Preview**: 3 plans, one highlighted.
7. **FAQ**: top objections (billing, attribution, setup time).
8. **Footer CTA**: final conversion prompt.

### 2. Pricing (`/pricing`)
1. Plan toggle (monthly/yearly).
2. Three-tier plan cards with usage caps.
3. Feature comparison table.
4. Add-ons (support, seats, managed services).
5. Billing FAQ + contact sales CTA.

### 3. Product (`/product`)
1. Outcome-focused hero.
2. Campaign workflow walkthrough.
3. Dashboard screenshots annotated by KPI impact.
4. Integrations grid.
5. Security/compliance mini section.

### 4. Login/Signup (`/login`, `/signup`)
1. Minimal fields.
2. SSO option.
3. Trust microcopy.
4. Error/help states and password rules.

---

## B. In-App Product Experience

### 5. App Shell (`/app`)
- Left nav: Dashboard, Campaigns, Audiences, Creatives, Analytics, Billing, Settings.
- Global top bar: account switcher, notifications, help, user menu.

### 6. Dashboard (`/app/dashboard`)
1. KPI strip (Spend, CTR, Conversions, CPA, ROAS).
2. Time-range selector.
3. Trend charts (Spend/CTR/Conv).
4. Alerts panel.
5. Top campaigns table.
6. Recent activity stream.

### 7. Campaigns List (`/app/campaigns`)
1. Filters (status, objective, date, channel).
2. Bulk actions (pause, resume, duplicate).
3. Table with sortable columns.
4. Inline edit for budget and schedule.

### 8. Campaign Builder (`/app/campaigns/new`)
1. Stepper: Objective → Audience → Creative → Budget → Review.
2. Real-time validation and policy hints.
3. Save draft at every step.
4. Summary panel (estimated reach, spend, expected KPI range).

### 9. Analytics (`/app/analytics`)
1. Overview cards + trend lines.
2. Attribution window selector.
3. Breakdown tables (campaign/audience/creative).
4. Export CTA (CSV/API).

### 10. Billing (`/app/billing`)
1. Current plan + usage meters.
2. Payment method management.
3. Invoice history.
4. Upgrade/downgrade controls with impact preview.

### 11. Settings (`/app/settings`)
1. Team roles and permissions.
2. Tracking integrations.
3. Brand safety / ad policy settings.
4. API keys and webhook settings.

---

## 11) Component Inventory (Design System Starter)

- Buttons (Primary/Secondary/Ghost/Destructive)
- Inputs (text, select, multiselect, date range)
- KPI Cards (with delta state)
- Data Table (sorting, filtering, pagination, bulk actions)
- Stepper (for campaign creation)
- Toast + inline alerts
- Empty/loading/error states
- Modal + drawer patterns
- Chart wrappers (line/bar/area with consistent legends)

---

## 12) Acceptance Criteria for the Redesign

### Conversion
- +15% improvement in signup completion rate.
- -20% reduction in time-to-first-campaign.

### Usability
- 90% of test users can publish first campaign without assistance.
- Critical tasks completed in <= 5 minutes for first-time user.

### Performance
- Landing LCP <= 2.5s on mobile.
- Dashboard INP <= 200ms for common interactions.

### Reliability
- No data-loss during campaign draft flow.
- Error states always provide recovery action.

---

## 13) Full Wireframe Spec — Desktop (1440px)

### Global Canvas
- Viewport target: **1440px width**
- Container max width: **1200px**
- Horizontal container padding: **24px**
- Grid: **12 columns**

### Section 1 — Navbar (70px height)
- Layout order: **Logo | Browse Ads | Categories | Post Ad (Primary) | Login**
- Logo left margin: **16px**
- Navigation center-left
- `Post Ad` sits right side and must be highest visual contrast CTA

### Section 2 — Hero (500–600px height)
- Two-column split:
  - **Left 40%**: H1, subheadline, large CTA
  - **Right 60%**: search container
- Left specs:
  - H1: **48px**, bold
  - Subtext: **18px**
  - CTA button height: **50px**
- Right specs:
  - Search box container padding: **24px**
  - Subtle shadow
  - Search fields: search input + category dropdown + location input
- UX intent: buyers use search, sellers click CTA (split flow)

### Section 3 — Trust Bar (80px height)
- Content: **Verified Users / No Spam / Fast Replies / UK Based**
- Horizontal icon+label rows with even spacing
- Background: light neutral tone

### Section 4 — Top Categories (≈300px)
- Show max **6–8 categories** only
- Card target size: **~180x140px**
- Grid options: **3x2** or **4x2**
- Adult categories should not appear in the top primary category area

### Section 5 — Latest Listings (core proof section)
- Grid of listing cards (live activity signal)
- Listing card includes: image, title, location, optional price
- Card width: **220–260px**
- Image height: **140px**
- Gap: **16–20px**

### Section 6 — Value Proposition
- Purpose: compare outcomes vs alternatives (cleaner, safer, faster responses)
- Layout: 2-column or centered icon+text stack

### Section 7 — Guarantee Block
- Message pattern: “Get replies in 24h or we boost again for free”
- Primary CTA: `Post Ad Now`

### Section 8 — Final CTA
- Example line: “Join early users getting more replies today”
- CTA: `Post Your Ad`

### Section 9 — Footer (≈200px)
- Links: Categories, Safety, Contact, Terms, About
- Trust utilities: Safety tips, Report user, Contact email

---

## 14) Visual Hierarchy & Critical UX Rules

### Priority order on first scan
1. Headline
2. Search or Post Ad CTA
3. Top categories
4. Latest listings

### Critical fixes
1. Reduce category clutter
2. Separate adult content from primary discovery surface
3. Add latest listings preview to prove activity
4. Make `Post Ad` CTA visually dominant

### Clean page flow
Navbar → Hero (split CTA/search) → Trust bar → Top categories → Latest listings → Value prop → Guarantee → Final CTA → Footer

---

## 15) Design System (Implementation Tokens)

### 15.1 Color palette
- **Primary**: `#2563EB` (hover `#1D4ED8`, active `#1E40AF`)
- **Secondary**: `#10B981`
- **Accent**: `#F59E0B`
- **Neutrals**:
  - Background `#FFFFFF`
  - Surface `#F9FAFB`
  - Border `#E5E7EB`
  - Text Primary `#111827`
  - Text Secondary `#6B7280`
- Ratio guideline: **60% neutral / 30% primary / 10% accent**

### 15.2 Typography
- Primary font: `Inter, system-ui, sans-serif`
- Type scale:
  - H1: 48px / 700
  - H2: 32px / 600
  - H3: 24px / 600
  - Body: 16px / 400
  - Small: 14px / 400
- Line-height: 1.4–1.6
- Rules:
  - Avoid body text under 16px for primary content
  - Left-align long-form text
  - Keep line length roughly 70–80 characters

### 15.3 Spacing (8px grid)
- Base unit: **8px**
- Scale: 4, 8, 16, 24, 32, 48, 64
- Usage examples:
  - Button horizontal padding: 16–24
  - Card gaps: 16–24
  - Section spacing: 48–64

### 15.4 Core components
- **Primary button**
  - Background: `#F59E0B`
  - Text: white
  - Height: 50px
  - Padding: `0 24px`
  - Radius: 8px
  - Weight: 600
- **Secondary button**
  - Border: `1px solid #E5E7EB`
  - Background: white
  - Text: `#111827`
- **Listing card**
  - Background: white
  - Border: `1px solid #E5E7EB`
  - Radius: 12px
  - Padding: 16px
  - Shadow: `0 2px 8px rgba(0,0,0,0.05)`
- **Search input**
  - Height: 56px
  - Radius: 12px
  - Border: `1px solid #E5E7EB`
  - Padding: `0 16px`

### 15.5 Responsive behavior
- Desktop cards per row: 3
- Tablet cards per row: 2
- Mobile cards per row: 1

### 15.6 Non-negotiable design rules
1. One primary action per section
2. Strong contrast on conversion actions
3. Reduce cognitive load by limiting simultaneous choices

---

## 16) Immediate Build Priorities (Do Today)

1. Add a `Latest Listings` section to homepage.
2. Reduce visible categories to top 6 on homepage.
3. Split hero into left CTA block and right search block.
4. Apply Inter font + 8px spacing system.
5. Update primary/secondary button and listing card styles to token values above.

course_description_to_market_research_report_prompt = """Given a course idea, you perform deep market research to indentify whether or not there is a valid market for that course idea.\n⸻\n\n0 · Is It Worth It? (Demand Score)\n\t1.\tMarket momentum — Does launching "[COURSE TOPIC]" make sense right now?\n\t2.\tDemand score — On a 0-to-10 scale, where does this niche rank and what percentile is that in education markets?\n\t3.\tRationale — Why is the score that high (or low)? Cite the key indicators.\n\n⸻\n\n1 · What We're Testing\n\t4.\tCourse focus — In one line, what core promise or transformation does the course deliver?\n\t5.\tIdeal learner — Who is the primary audience?\n\t6.\tDelivery format — How many modules, what media (video, checklists, live calls, etc.)?\n\t7.\tGap analysis — Which scattered resources are we unifying, and why does that matter?\n\t8.\tKey content pillars — List the 3-4 most critical learning outcomes.\n\n⸻\n\n2 · Big Trends\n\t9.\tSearch trajectory — What is the 5-year Google search trend (+/- %) for "[COURSE TOPIC]"?\n\t10.\tSocial-media signals — How fast are top influencers or communities in this space growing?\n\t11.\tMacro forces — Which cultural, economic, or regulatory shifts are accelerating interest?\n\n⸻\n\n3 · Who's Out There (Competitor Landscape)\n\t12.\tTop competitors — For each of three current courses, provide the following fields: courseName, websiteUrl (main domain or product page), logoUrl (https://logo.clearbit.com/{domain}), strengths, weaknesses, priceUSD.\n\t13.\tOpportunity gap — Where can our course clearly outperform or differentiate?\n\n⸻\n\n4 · Learner Worries / Pain Points\n\t14.\tPrimary anxieties — What keeps prospective students up at night (top 3-4 concerns)?\n\t15.\tEvidence — Which surveys, forums, or social threads confirm these worries (> 70 % mention rate)?\n\n⸻\n\n5 · What They'll Pay\n\t16.\tWillingness-to-pay — What price feels comfortable for a comprehensive solution in this niche?\n\t17.\tBenchmarking — How does that compare to 60+ similar programs or info products?\n\n⸻\n\n6 · Should We Build It?\n\t18.\tGo / No-go — Given demand, competition gaps, and price point, should we proceed?\n\t19.\tCore justification — Summarize the single biggest reason to move forward (or not).\n\n⸻\n\n7 · 1-Year Revenue Outlook\n\t20.\tBad scenario — If traction is weak, how many students enroll?\n\t21.\tGood scenario — With solid demand, same questions.\n\t22.\tExcellent scenario — If the course over-performs, same questions.\n\t23.\tIndustry average — What's the typical 12-month revenue for comparable courses?\n\t24.\tLikely outcome — Project the most probable revenue 12 months post-launch and the percentage difference vs. the industry average.\n\t25.\tScenario drivers — Which levers (audience size, ad spend, referrals, pricing) most influence shifts between scenarios?"""
market_report_prompt = """Given a market research report, restructure its insights into window.courseData as a single-line JavaScript assignment following the full structure and data types of the example below. Your output must start with window.courseData= and end with ;, with all data in the shown key order. Use *only* light-mode brandColors (background, primary, text, textSecondary, accent, border) and **do not** include a darkMode object. For each of the top three competitors, include both a websiteUrl and a logoUrl field. Only output valid JavaScript—no line breaks, no comments, no extra text. Example output: window.courseData={brandColors:{background:"#F6F9FC",primary:"#0A2540",text:"#1F2937",textSecondary:"#4B5563",accent:"#3B82F6",border:"#E5E7EB"},meta:{courseTitle:"Stripe Revenue Recovery Bootcamp",reportTitle:"Stripe Failed-Payment Market Snapshot 2025"},demand:{score:7.8,percentile:84,question:"Should you create a Stripe revenue-recovery course?",answer:"Yes—demand is high and pressing.",why:"• Subscription spend is > 50 % of U.S. software outlays, yet involuntary churn still erodes 9–15 % of MRR for SMB SaaS. • Google searches for "Stripe failed payment" and related keywords are up 38 % vs 2020. • Few hands-on programs serve RevOps leads; every extra 1 % recovered revenue lifts valuation 3–4 %."},testing:{overview:"Cut involuntary churn by 30–50 % in 60 days using Stripe's recovery stack and proven playbooks.",targetAudience:"Seed-to-Series-B SaaS founders, RevOps managers, and senior developers already using Stripe.",format:"4-week cohort: 8 modules, ≈5 h HD video, copy + code swipe files, ROI calculator, 2 live clinics, private Slack.",question:"Why this course over free docs or webinars?",answer:"It unites technical execution (webhooks, Smart Retries) with revenue-ops strategy (KPIs, messaging) in one ROI-backed package.",why:"Current resources are siloed—Stripe docs are developer-centric; ProfitWell webinars are product-led. No single source bridges both worlds for small teams.",contentPillars:["Root-cause analytics of payment failures","Smart Retries, Adaptive Acceptance & webhook logic","High-converting 7-touch dunning cadences (email/SMS/localization)","Compliance, disputes & tracking 'Recovered MRR'"]},trends:{googleSearchChangePct:51,socialMediaGrowthPct:26,macroFactor:"Net-revenue-retention scrutiny, Visa CE 3.0 dispute rules, and expensive capital make revenue recovery the cheapest growth lever.",question:"Is interest still climbing?",answer:"Yes—searches, subreddit growth and newsletter sign-ups are all accelerating.",why:"• 'Stripe failed payment' +74 % in 5 yrs • r/Stripe tripled members in < 3 yrs • Patrick McKenzie's payment-failure newsletter tripled subscribers (14 k→43 k)"},competitors:{question:"Who else teaches Stripe payment recovery?",answer:"Only three notable options, none offer a vendor-specific yet product-agnostic, ROI-guaranteed cohort.",why:"Udemy is beginner-centric, LevelUp is dev-only, ProfitWell Retain is a lead-gen funnel locked to their tool.",list:[{name:"Udemy — Stripe Payments Masterclass 2024",strengths:"Low price, solid step-by-step setup",weaknesses:"Lacks advanced retries, dunning, or KPI focus",priceUSD:19.99,websiteUrl:"https://www.udemy.com/course/stripe-payments-masterclass/",logoUrl:"https://s.udemycdn.com/meta/default-meta-image-v2.png"},{name:"LevelUp Tutorials — Modern Payments with Stripe",strengths:"In-depth code demos",weaknesses:"Developer-centric; minimal RevOps or compliance content",priceUSD:249,websiteUrl:"https://leveluptutorials.com/tutorials/modern-payments-with-stripe",logoUrl:"https://leveluptutorials.com/favicon.ico"},{name:"ProfitWell Retain Workshops",strengths:"Great benchmarks, strategic framing",weaknesses:"Free but tied to ProfitWell product; Stripe feature depth shallow",priceUSD:0,websiteUrl:"https://www.profitwell.com/retain",logoUrl:"https://www.profitwell.com/favicon.ico"}]},worries:{question:"What keeps learners up at night?",answer:"Revenue leakage, technical uncertainty, and compliance risk.",why:"Surveys and conference panels show ≥ 70 % citing failed payments as a top churn driver and Stripe docs as too technical.",topConcerns:[""We lose 10 % of customers monthly and don't know why."","Stripe docs are too technical; ops can't translate them."","Chargebacks are spiking—are we at risk of account termination?","Generic dunning emails aren't moving the needle.""]},pricing:{question:"What will the market pay?",answer:"$499 list (≈$399 after promos) positions us at the 65th percentile of comparable B2B tech courses.",why:"SMB SaaS execs will pay $300–800 if ROI ≥ 10×. Median benchmark is $397; $499 signals premium yet attainable.",targetPriceUSD:499},buildDecision:{question:"Based on the data, should we build it?",answer:"GO.",why:"High pain, scarce competition, and clear financial upside for learners give first-mover advantage."},revenueOutlook:{launchTimelineDays:45,likelyRevenueUSD:59800,industryAverageUSD:75000,scenarios:[{name:"Lower",students:50,priceUSD:399,revenueUSD:19900},{name:"Mid",students:150,priceUSD:399,revenueUSD:59850},{name:"High",students:500,priceUSD:399,revenueUSD:199500}],question:"What's the 12-month upside?",answer:"Realistically ≈ $60 k gross on a 150-student year-one cohort; upside to $200 k with breakout reach.",why:"Assumes 20 % promo rate, list + partner reach of 8–10 k founders, and 1.5–2 % funnel conversion."},opportunityScore:83};"""


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title id="pageTitle"></title>

  <!-- Tailwind 3 – CDN build (JIT) -->
  <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
  <script>
    /* Minimal Tailwind config (no dark mode) */
    tailwind.config = {
      theme: {
        extend: {
          boxShadow: {
            brand: '0 8px 28px rgba(0,0,0,.06), 0 2px 8px rgba(0,0,0,.04)',
          },
        }
      }
    }
  </script>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.gstatic.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400..800&display=swap" rel="stylesheet" />

  <!-- Chart.js + plugins -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.2.0" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@1.4.0/dist/chartjs-plugin-annotation.min.js" defer></script>

  <!-- Hero-icon-js -->
  <script src="https://cdn.jsdelivr.net/npm/hero-icon-js/hero-icon-outline.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/hero-icon-js/hero-icon-solid.min.js" defer></script>

  <style>
    /* ========== 1. CSS Variables (light only) ========== */
    :root {
      --light-bg:         #ffffff;
      --light-primary:    #0a2540;
      --light-text:       #1f2937;
      --light-text2:      #4b5563;
      --light-accent:     #3b82f6;
      --light-border:     #e5e7eb;

      --background:       var(--light-bg);
      --primary:          var(--light-primary);
      --text-strong:      var(--light-text);
      --text-soft:        var(--light-text2);
      --accent:           var(--light-accent);
      --border:           var(--light-border);
    }

    /* ========== 2. Base styles & utilities ========== */
    html {
      font-family: 'Inter', system-ui, sans-serif;
      background: var(--background);
      color: var(--text-strong);
    }
    body {
      min-height: 100vh;
    }
    ::selection {
      background: var(--accent);
      color: #fff;
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 10px;
      height: 10px;
    }
    ::-webkit-scrollbar-thumb {
      background: var(--border);
      border-radius: 8px;
    }

    /* Reveal-on-scroll */
    .reveal {
      opacity: 0;
      transform: translateY(28px);
      transition: opacity .6s, transform .6s;
    }
    .reveal.visible {
      opacity: 1;
      transform: none;
    }

    /* Sticky table header on ≥lg */
    @media (min-width:1024px) {
      thead.table-header-sticky {
        position: sticky; 
        top: 0; 
        backdrop-filter: blur(8px);
      }
    }
  </style>
</head>

<body class="lg:grid lg:grid-cols-[260px_minmax(0,1fr)] antialiased">

  <!-- Skip link for accessibility -->
  <a href="#content" class="sr-only focus:not-sr-only focus:absolute focus:top-3 focus:left-3 bg-[var(--primary)] text-white rounded px-3 py-1 z-50">
    Skip to content
  </a>

  <!-- ───────────────────────  SIDEBAR  ─────────────────────── -->
  <aside id="toc"
    class="hidden lg:block sticky top-0 h-screen overflow-y-auto border-r 
           border-[var(--border)] bg-[var(--background)] p-6 z-30"
    aria-label="Table of contents">
    <header class="flex justify-between items-center mb-6">
      <h2 class="uppercase tracking-wide font-semibold text-xs text-[var(--text-soft)]">On this page</h2>
      <!-- (Removed theme toggle button) -->
    </header>
    <nav id="tocLinks" class="space-y-2 leading-6 text-sm"></nav>
  </aside>

  <!-- ───────────────────────  MAIN  ─────────────────────── -->
  <main id="content" class="px-4 sm:px-6 py-14">
    <!-- HERO / HEADER -->
    <header
      class="relative rounded-xl mb-8 reveal visible overflow-hidden
             bg-gradient-to-br from-[var(--primary)] to-[var(--primary)]/70 text-white 
             shadow-brand">
      <div class="px-6 py-14 sm:py-20 text-center">
        <h1 id="courseTitle" class="text-4xl sm:text-5xl font-extrabold"></h1>
        <p id="reportSubtitle" class="mt-4 text-lg/relaxed text-white/90"></p>
      </div>
      <span id="opportunityScore"
        class="absolute top-4 right-4 sm:right-8 bg-black/10 
               backdrop-blur px-4 py-1 rounded-full text-sm font-semibold">
      </span>
    </header>

    <!-- KPI SUMMARY -->
    <section id="kpiSummary"
      class="grid grid-cols-2 sm:grid-cols-4 gap-4 text-center text-sm mb-10
             bg-[var(--background)] shadow-brand ring-1 ring-black/5 
             rounded-xl p-5 reveal">
    </section>

    <!-- Nav (hamburger) for mobile -->
    <button id="tocToggle"
      class="lg:hidden fixed bottom-6 right-6 z-[60] bg-[var(--primary)] text-white p-3 
             rounded-full shadow-brand focus:ring-4 ring-[var(--primary)]/50"
      aria-controls="toc" aria-expanded="false">
      <hero-icon-outline name="bars-3" class="w-6 h-6"></hero-icon-outline>
    </button>

    <!-- Template for dynamic sections -->
    <template id="sectionTemplate">
      <section
        class="reveal mb-14 rounded-xl ring-1 ring-black/5 shadow-brand 
               bg-[var(--background)] lg:grid lg:grid-cols-[minmax(0,680px)_1fr] 
               lg:gap-12 p-8 space-y-6">
        <div>
          <div class="flex items-center gap-3 mb-4">
            <span class="icon-wrap shrink-0"></span>
            <h2 class="title text-2xl font-bold tracking-tight text-[var(--primary)]"></h2>
          </div>
          <div class="section-body prose max-w-none"></div>
        </div>
        <div class="section-chart-col flex items-center justify-center mt-4 lg:mt-0"></div>
      </section>
    </template>

    <!-- Final verdict placeholder (will be populated via JS) -->
    <section id="verdict" class="hidden"></section>
  </main>

  <!-- Desktop CTA (Back-to-top) -->
  <div id="ctaBar"
    class="hidden lg:flex fixed bottom-6 right-6 items-center gap-4
           bg-[var(--primary)] text-white px-6 py-3 rounded-full shadow-brand z-[55]">
    <button class="font-semibold hover:bg-white/10 px-3 py-1 rounded focus:ring-2 ring-inset ring-white/60"
            onclick="window.scrollTo({top:0,behavior:'smooth'})">↑ Top</button>
  </div>

  <!-- ───────────────────────  AUDIO BAR w/ React  ─────────────────────── -->
  <div id="react-root"></div>

  <!-- ───────────────────────  SCRIPTS  ─────────────────────── -->
  <script>
/* -----------------------------------------------------------
   Helper: loadScript(url)  (returns Promise)
------------------------------------------------------------*/
function loadScript(url) {
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    s.src = url;
    s.onload = resolve;
    s.onerror = () => reject(new Error('Failed to load ' + url));
    document.head.appendChild(s);
  });
}

/* -----------------------------------------------------------
   Heroicon helper
------------------------------------------------------------*/
function icon(name, cls='w-6 h-6 text-[var(--primary)]'){
  return `<hero-icon-outline name="${name}" class="${cls}"></hero-icon-outline>`;
}

/* -----------------------------------------------------------
   Load external COURSE DATA script, then build UI
   Replace CUSTOM_VALUES_MARKET_RESEARCH_REPORT with your script URL
------------------------------------------------------------*/
document.addEventListener('DOMContentLoaded', async () => {
  try {
    await loadScript(CUSTOM_VALUES_MARKET_RESEARCH_REPORT); // Must define window.courseData
    buildPage();
  } catch (e) {
    console.error(e);
  }
});

/* -----------------------------------------------------------
   Apply brandColors (light only)
------------------------------------------------------------*/
function applyBrandColors(bc) {
  // We only read bc.lightMode here (always light)
  if (!bc.lightMode) return;
  document.documentElement.style.setProperty('--light-bg',         bc.lightMode.background     || '#ffffff');
  document.documentElement.style.setProperty('--light-primary',    bc.lightMode.primary       || '#0a2540');
  document.documentElement.style.setProperty('--light-text',       bc.lightMode.text          || '#1f2937');
  document.documentElement.style.setProperty('--light-text2',      bc.lightMode.textSecondary || '#4b5563');
  document.documentElement.style.setProperty('--light-accent',     bc.lightMode.accent        || '#3b82f6');
  document.documentElement.style.setProperty('--light-border',     bc.lightMode.border        || '#e5e7eb');
}

function buildPage() {
  if (!window.courseData) {
    return console.error('courseData missing');
  }
  const d = window.courseData;

  // 1. Apply brandColors (light only)
  if(d.brandColors) {
    applyBrandColors(d.brandColors);
  }

  // 2. Title & header info
  const pageTitle = `${d.meta.courseTitle} · ${d.meta.reportTitle}`;
  document.title = pageTitle;
  document.getElementById('pageTitle').textContent = pageTitle;
  document.getElementById('courseTitle').textContent = d.meta.courseTitle;
  document.getElementById('reportSubtitle').textContent = d.meta.reportTitle;
  document.getElementById('opportunityScore').textContent = `Score ${d.opportunityScore}/100`;

  // 3. TOC setup
  const tocData = [
    ['worthIt','Should You Make It?','light-bulb'],
    ['overview','Course Overview','book-open'],
    ['trends','Market Trends','chart-bar'],
    ['competitors','Competition','users'],
    ['worries','Learner Concerns','exclamation-triangle'],
    ['pricing','Ideal Pricing','currency-dollar'],
    ['outlook','Revenue Outlook','chart-pie'],
    ['verdict','Conclusion','check-circle']
  ];
  const tocLinks = document.getElementById('tocLinks');
  tocData.forEach(([id,label,heroIcon]) => {
    const a = document.createElement('a');
    a.href = '#'+id;
    a.className = 'block px-3 py-1 rounded hover:text-[var(--primary)] transition-colors';
    a.innerHTML = label;
    tocLinks.appendChild(a);
  });

  // hamburger toggle
  const tocDrawer = document.getElementById('toc');
  const tocToggle = document.getElementById('tocToggle');
  tocToggle.onclick = () => {
    tocDrawer.classList.toggle('hidden');
    const expanded = !tocDrawer.classList.contains('hidden');
    tocToggle.setAttribute('aria-expanded', expanded);
  };

  // 4. Build dynamic sections
  const main = document.querySelector('main');
  const template = document.getElementById('sectionTemplate');

  const sectionsData = [
    {
      id:'worthIt', icon:'light-bulb', title:'1 · Should You Make It?',
      html: `
        <div class="flex flex-wrap gap-2 text-sm mb-6">
          <span class="px-3 py-1 rounded-full bg-emerald-100 text-emerald-800">
            Demand Score <strong>${d.demand.score}/10</strong>
          </span>
          <span class="px-3 py-1 rounded-full bg-blue-100 text-blue-800">
            Top <strong>${d.demand.percentile}%</strong>
          </span>
        </div>
        <p class="italic mb-2"><strong>Question:</strong> "${d.demand.question}"</p>
        <p><strong>Answer:</strong> ${d.demand.answer}</p>
        <p><strong>Why:</strong> ${d.demand.why}</p>
      `,
      chart:'scoreChart',
    },
    {
      id:'overview', icon:'book-open', title:'2 · Course Overview',
      html: `
        <div class="flex flex-wrap gap-2 text-sm mb-4">
          <span class="chip">Overview:&nbsp;<strong>${d.testing.overview}</strong></span>
          <span class="chip">Audience:&nbsp;<strong>${d.testing.targetAudience}</strong></span>
          <span class="chip">Format:&nbsp;<strong>${d.testing.format}</strong></span>
        </div>
        <p class="italic mb-2"><strong>Question:</strong> "${d.testing.question}"</p>
        <p><strong>Answer:</strong> ${d.testing.answer}</p>
        <p><strong>Why:</strong> ${d.testing.why}</p>
        <ul class="list-disc list-inside grid sm:grid-cols-2 gap-x-6 mt-4 text-sm">
          ${ d.testing.contentPillars.map(p=>`<li>${p}</li>`).join('') }
        </ul>
      `,
    },
    {
      id:'trends', icon:'chart-bar', title:'3 · Market Trends',
      html: `
        <div class="flex flex-wrap gap-2 text-sm mb-4">
          <span class="chip bg-emerald-100 text-emerald-800">
            Google +${d.trends.googleSearchChangePct}%
          </span>
          <span class="chip bg-cyan-100 text-cyan-800">
            Social +${d.trends.socialMediaGrowthPct}%
          </span>
          <span class="chip">${d.trends.macroFactor}</span>
        </div>
        <p class="italic mb-2"><strong>Question:</strong> "${d.trends.question}"</p>
        <p><strong>Answer:</strong> ${d.trends.answer}</p>
        <p><strong>Why:</strong> ${d.trends.why}</p>
      `,
      chart:'trendChart',
    },
    {
      id:'competitors', icon:'users', title:'4 · Competition',
      html: `
        <p class="italic mb-2"><strong>Question:</strong> "${d.competitors.question}"</p>
        <p><strong>Answer:</strong> ${d.competitors.answer}</p>
        <p><strong>Why:</strong> ${d.competitors.why}</p>
        <div class="overflow-x-auto mt-4">
          <table class="min-w-full text-sm whitespace-nowrap">
            <thead class="table-header-sticky bg-[var(--background)] text-[var(--text-strong)]">
              <tr>
                <th class="py-2 px-4 font-semibold">Resource</th>
                <th class="py-2 px-4 font-semibold">Strengths</th>
                <th class="py-2 px-4 font-semibold">Weaknesses</th>
                <th class="py-2 px-4 font-semibold text-right">Price</th>
              </tr>
            </thead>
            <tbody id="competitorTable" class="divide-y divide-[var(--border)]"></tbody>
          </table>
        </div>
      `,
    },
    {
      id:'worries', icon:'exclamation-triangle', title:'5 · Learner Concerns',
      html: `
        <p class="italic mb-2"><strong>Question:</strong> "${d.worries.question}"</p>
        <p><strong>Answer:</strong> ${d.worries.answer}</p>
        <p><strong>Why:</strong> ${d.worries.why}</p>
        <ul class="list-disc list-inside grid sm:grid-cols-2 gap-x-6 mt-4 text-sm">
          ${ d.worries.topConcerns.map(c=>`<li>${c}</li>`).join('') }
        </ul>
      `,
    },
    {
      id:'pricing', icon:'currency-dollar', title:'6 · Ideal Pricing',
      html: `
        <p class="italic mb-2"><strong>Question:</strong> "${d.pricing.question}"</p>
        <p><strong>Answer:</strong> ${d.pricing.answer}</p>
        <p><strong>Why:</strong> ${d.pricing.why}</p>
      `,
      chart:'priceChart',
    },
    {
      id:'outlook', icon:'chart-pie', title:'7 · Revenue Outlook',
      html: `
        <div class="flex flex-wrap gap-2 text-sm mb-4">
          <span class="chip bg-emerald-100 text-emerald-800">
            Likely $${d.revenueOutlook.likelyRevenueUSD}
          </span>
          <span class="chip bg-blue-100 text-blue-800">
            vs $${d.revenueOutlook.industryAverageUSD} avg
          </span>
          <span class="chip bg-purple-100 text-purple-800">
            Launch in ${d.revenueOutlook.launchTimelineDays} days
          </span>
        </div>
        <p class="italic mb-2"><strong>Question:</strong> "${d.revenueOutlook.question}"</p>
        <p><strong>Answer:</strong> ${d.revenueOutlook.answer}</p>
        <p><strong>Why:</strong> ${d.revenueOutlook.why}</p>

        <div class="overflow-x-auto mt-4">
          <table class="min-w-full text-sm whitespace-nowrap">
            <thead class="table-header-sticky bg-[var(--background)] text-[var(--text-strong)]">
              <tr>
                <th class="py-2 px-4 font-semibold">Scenario</th>
                <th class="py-2 px-4 font-semibold">Students</th>
                <th class="py-2 px-4 font-semibold">Price</th>
                <th class="py-2 px-4 font-semibold text-right">12-Mo Revenue</th>
              </tr>
            </thead>
            <tbody id="scenarioTable" class="divide-y divide-[var(--border)]"></tbody>
          </table>
        </div>
      `,
      chart:'outlookChart',
    },
    {
      id:'verdict', icon:'check-circle', title:'8 · Conclusion',
      html: `
        <p class="italic mb-2"><strong>Question:</strong> "${d.buildDecision.question}"</p>
        <p><strong>Answer:</strong> ${d.buildDecision.answer}</p>
        <p><strong>Why:</strong> ${d.buildDecision.why}</p>
      `,
    }
  ];

  sectionsData.forEach(sec => {
    const content = template.content.cloneNode(true);
    const sectionEl = content.querySelector('section');
    sectionEl.id = sec.id;
    content.querySelector('.icon-wrap').innerHTML = icon(sec.icon);
    content.querySelector('.title').textContent = sec.title;
    content.querySelector('.section-body').innerHTML = sec.html;
    if(sec.chart) {
      content.querySelector('.section-chart-col').innerHTML = `<canvas id="${sec.chart}" class="max-w-full h-64" role="img"></canvas>`;
    } else {
      content.querySelector('.section-chart-col').remove();
    }
    main.appendChild(content);
  });

  // 5. KPI summary
  document.getElementById('kpiSummary').innerHTML = `
    <div>
      <div class="font-semibold">Demand</div>
      <div>${d.demand.score}/10</div>
    </div>
    <div>
      <div class="font-semibold">Target Price</div>
      <div>$${d.pricing.targetPriceUSD}</div>
    </div>
    <div>
      <div class="font-semibold">Likely 12-mo Rev</div>
      <div>$${d.revenueOutlook.likelyRevenueUSD}</div>
    </div>
    <div>
      <div class="font-semibold">Launch Time</div>
      <div>${d.revenueOutlook.launchTimelineDays} days</div>
    </div>
  `;

  // 6. Competitors & Scenarios
  const compTbody = document.getElementById('competitorTable');
  d.competitors.list.forEach(row => {
    const tr = document.createElement('tr');
    tr.className = 'hover:bg-[var(--primary)]/5';
    tr.innerHTML = `
      <td class="py-2 px-4">${row.name}</td>
      <td class="py-2 px-4">${row.strengths}</td>
      <td class="py-2 px-4">${row.weaknesses}</td>
      <td class="py-2 px-4 text-right">$${row.priceUSD}</td>
    `;
    compTbody.appendChild(tr);
  });
/* 2️⃣  Fix the colour + Y-offset and draw the score  */
/* ── Replace your current score-label plugin with this ───────────────── */
/* ───────────────── score inside the arc ───────────────── */
function scoreHue(score /* 0-10 */) {
  /* 0  → hue 0  (red)
     10 → hue 120 (green) */
  return `hsl(${Math.round(score * 12)}, 85%, 45%)`;
}

/* ── 2. Label plug-in (centre of arc) ────────────────────────────── */
const scoreLabelPlugin = {
  id: 'scoreLabel',
  afterDatasetsDraw(chart, _args, { text, colour }) {
    if (chart.canvas.id !== 'scoreChart') return;

    const arc = chart.getDatasetMeta(0).data[0];
    const cx  = arc.x;
    const cy  = arc.y;
    const y   = cy - arc.innerRadius * 0.50;   // halfway between centre and arc

    const { ctx } = chart;
    ctx.save();
    ctx.font         = '600 22px "Inter", sans-serif';
    ctx.textAlign    = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillStyle    = colour;                // same hue as arc
    ctx.fillText(text, cx, y);
    ctx.restore();
  }
};
Chart.register(scoreLabelPlugin);
  const scenarioTbody = document.getElementById('scenarioTable');
  d.revenueOutlook.scenarios.forEach(s => {
    const tr = document.createElement('tr');
    tr.className = 'hover:bg-[var(--primary)]/5';
    tr.innerHTML = `
      <td class="py-2 px-4">${s.name}</td>
      <td class="py-2 px-4">${s.students.toLocaleString()}</td>
      <td class="py-2 px-4">$${s.priceUSD}</td>
      <td class="py-2 px-4 text-right">$${s.revenueUSD.toLocaleString()}</td>
    `;
    scenarioTbody.appendChild(tr);
  });

  // 7. Charts (fixed light colors)
  Chart.defaults.color       = '#475569';
  Chart.defaults.borderColor = '#cbd5e1';

  // Demand half-doughnut
/* ── 3. Build the chart ──────────────────────────────────────────── */
if (document.getElementById('scoreChart')) {
  const score   = d.demand.score;                 // e.g. 7.2
  const colour  = scoreHue(score);                // e.g. hsl(86,85%,45%)

  new Chart(scoreChart, {
    type : 'doughnut',
    data : {
      labels   : ['Score', 'Remaining'],
      datasets : [{
        data            : [score, 10 - score],
        backgroundColor : [colour, 'var(--border)'],
        borderWidth     : 0,
        cutout          : '70%'
      }]
    },
    options : {
      rotation     : -90,
      circumference: 180,
      plugins      : {
        legend :  { display: false },
        tooltip:  { enabled: false },
        scoreLabel: { text: `${score.toFixed(1)}/10`, colour }
      },
      animation: { duration: 800, easing: 'easeOutQuart' }  // nice sweep-in
    }
  });
}
  // Market trends line
  if(document.getElementById('trendChart')) {
    new Chart(trendChart, {
      type:'line',
      data:{
        labels: d.trends.years ?? ['2019','2020','2021','2022','2023'],
        datasets:[{
          data: d.trends.index ?? [100,110,120,130,140],
          borderColor:'var(--primary)',
          fill:false,
          tension:0.35
        }]
      },
      options:{
        plugins:{legend:{display:false}},
        scales:{y:{ticks:{callback:v=>v+'%'}}}
      }
    });
  }

  // Ideal Pricing donut with center text
  if(document.getElementById('priceChart')){
    const centerTextPlugin = {
      id:'ct',
      afterDraw(c) {
        if(c.canvas.id!=='priceChart') return;
        const {ctx, chartArea:{left,right,top,bottom}} = c;
        ctx.save();
        ctx.font='600 24px Inter';
        ctx.textAlign='center';
        ctx.textBaseline='middle';
        ctx.fillStyle= '#111827';
        ctx.fillText('$'+d.pricing.targetPriceUSD, (left+right)/2, (top+bottom)/2);
        ctx.restore();
      }
    };
    Chart.register(centerTextPlugin);

    new Chart(priceChart, {
      type:'doughnut',
      data:{
        labels:['target',''],
        datasets:[{
          data:[ d.pricing.targetPriceUSD, 300 ],
          backgroundColor:[
            'var(--primary)',
            'var(--border)'
          ],
          borderWidth:0,
          cutout:'65%'
        }]
      },
      options:{
        plugins:{legend:{display:false}}
      }
    });
  }

  // Revenue outlook bar
  if(document.getElementById('outlookChart')){
    new Chart(outlookChart, {
      type:'bar',
      data:{
        labels: d.revenueOutlook.scenarios.map(s=>s.name),
        datasets:[
          {
            data: d.revenueOutlook.scenarios.map(s=>s.revenueUSD),
            backgroundColor:['#f87171','#fbbf24','#34d399'],
            borderRadius:6,
            borderSkipped:false
          }
        ]
      },
      options:{
        plugins:{
          legend:{display:false},
          annotation:{
            annotations:{
              avg:{
                type:'line',
                yMin:d.revenueOutlook.industryAverageUSD,
                yMax:d.revenueOutlook.industryAverageUSD,
                borderColor:'#475569',
                borderDash:[6,6],
                borderWidth:1.5,
                label:{
                  content:`Avg $${d.revenueOutlook.industryAverageUSD.toLocaleString()}`,
                  enabled:true,
                  color:'#fff',
                  backgroundColor:'rgba(0,0,0,.65)',
                  font:{style:'italic'},
                  yAdjust:-6
                }
              }
            }
          },
          tooltip:{
            callbacks:{label: ctx => '$'+ctx.parsed.y.toLocaleString()}
          }
        },
        scales:{
          y:{
            beginAtZero:true,
            ticks:{callback:v=>'$'+(v/1000)+'k'}
          }
        }
      }
    });
  }

  // 8. ScrollSpy
  const tocAnchors = [...document.querySelectorAll('#tocLinks a')];
  const watchSections = tocAnchors.map(a=>document.getElementById(a.hash.slice(1)));

  const spy = new IntersectionObserver(entries => {
    entries.forEach(ent=>{
      if(ent.isIntersecting) {
        tocAnchors.forEach(l=>l.classList.remove('text-[var(--primary)]','font-semibold'));
        const current = tocAnchors.find(l=>l.hash.slice(1) === ent.target.id);
        if(current) current.classList.add('text-[var(--primary)]','font-semibold');
      }
    });
  }, {rootMargin:'-35% 0px -50%'});

  watchSections.forEach(s=>spy.observe(s));

  // 9. Reveal on scroll
  const revealObs = new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(e.isIntersecting) {
        e.target.classList.add('visible');
      }
    });
  },{ threshold:.1 });
  document.querySelectorAll('.reveal').forEach(el=>revealObs.observe(el));
}


/* ==========  React Audio Player  ========== */
(async()=>{
  await loadScript('https://unpkg.com/react@18/umd/react.production.min.js');
  await loadScript('https://unpkg.com/react-dom@18/umd/react-dom.production.min.js');
  const {useRef,useState,useEffect} = React;

  const fmt = (t) => `${Math.floor(t/60)}:${String(Math.floor(t%60)).padStart(2,'0')}`;
/* -----------------------------------------------------------
   Chart: Gauge (for demand score)
------------------------------------------------------------*/
function createGaugeChart(score, percentile) {
  const canvas = document.createElement('canvas');
  canvas.width = 220;
  canvas.height = 140;

  const data = {
    datasets: [{
      data: [score, 10 - score],
      backgroundColor: [
        `hsl(${score * 12}, 80%, 50%)`, // Hue from red (0) to green (120)
        'var(--border)'
      ],
      borderWidth: 0,
      circumference: 180,
      rotation: 270,
    }]
  };

  new Chart(canvas, {
    type: 'doughnut',
    data: data,
    options: {
      responsive: false,
      cutout: '70%',
      plugins: {
        legend: { display: false },
        tooltip: { enabled: false },
        datalabels: {
          formatter: () => '',
        },
        annotation: {
          annotations: {
            percentileText: {
              type: 'label',
              content: [`Top ${Math.round(percentile)}%`],
              x: '50%',
              y: '98%',
              font: { size: 13, weight: '500' },
              color: 'var(--text-soft)',
              textAlign: 'center',
            }
          }
        }
      }
    },
    plugins: [{
      id: 'gaugeText',
      afterDatasetsDraw(chart, args, options) {
        const { ctx, chartArea: { bottom, width } } = chart;
        const x = width / 2;
        const y = bottom - 15;

        ctx.save();
        ctx.font = `600 44px Inter, sans-serif`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'bottom';
        ctx.fillStyle = `hsl(${score * 12}, 70%, 40%)`;
        ctx.fillText(score.toFixed(1), x, y);
        ctx.restore();
      }
    }]
  });
  return canvas;
}
  function Player() {
    const audioRef = useRef(null);
    const [play,setPlay] = useState(false);
    const [curr,setCurr] = useState(0);
    const [dur,setDur]   = useState(0);
    const [spd,setSpd]   = useState(1);

    useEffect(()=>{
      const audio = audioRef.current;
      const meta = ()=> setDur(audio.duration||0);
      const prog = ()=> setCurr(audio.currentTime||0);
      audio.addEventListener('loadedmetadata', meta);
      audio.addEventListener('timeupdate', prog);
      return()=>{
        audio.removeEventListener('loadedmetadata', meta);
        audio.removeEventListener('timeupdate', prog);
      }
    },[]);

    return React.createElement(
      'div',
      { className:'fixed bottom-4 left-1/2 -translate-x-1/2 z-[70] w-[95%] max-w-3xl flex items-center gap-4 px-5 py-3 rounded-xl text-white bg-black/70 backdrop-blur shadow-brand ring-1 ring-white/10' },
      React.createElement(
        'button',
        {
          onClick: () => {
            const a=audioRef.current;
            if(play) a.pause(); else a.play();
            setPlay(!play);
          },
          className:'w-14 h-14 grid place-items-center rounded-full bg-[var(--primary)] shadow ring-1 ring-white/10'
        },
        React.createElement(
          'hero-icon-solid',
          { name: play ? 'pause' : 'play', class:'w-7 h-7' }
        )
      ),
      React.createElement(
        'div',
        { className:'flex-1' },
        React.createElement(
          'div',
          { className:'flex justify-between text-xs text-gray-200 mb-1' },
          React.createElement('span',null,'Market Research Summary'),
          React.createElement('span',null, fmt(curr)+' / '+fmt(dur))
        ),
        React.createElement('input',{
          type:'range',
          value: dur ? (curr/dur)*100 : 0,
          onChange: e=>{
            audioRef.current.currentTime = (e.target.value/100)*dur;
          },
          className:'w-full accent-[var(--primary)]'
        })
      ),
      React.createElement(
        'select',
        {
          value:spd,
          onChange: e=>{
            setSpd(e.target.value);
            audioRef.current.playbackRate = e.target.value;
          },
          className:'text-xs bg-gray-800 border border-gray-700 rounded px-2 py-1'
        },
        [0.75,1,1.25,1.5,2].map(v=>React.createElement('option',{key:v,value:v},v+'x'))
      ),
      React.createElement('audio',{ref:audioRef,src:AUDIO_EXPLAINATION,preload:'metadata'})
    );
  }

  ReactDOM.createRoot(document.getElementById('react-root')).render(React.createElement(Player));
})();
  </script>

  <!-- Tiny chip utility + actionBtn classes (light only) -->
  <style>
    .chip {
      @apply px-3 py-1 rounded-full bg-[var(--border)] text-[var(--text-strong)];
    }
    .actionBtn {
      @apply bg-[var(--primary)] text-white px-4 py-2 rounded-full shadow-brand 
             hover:bg-[var(--primary)]/90 focus:ring-2 ring-[var(--primary)]/60 transition;
    }
  </style>
</body>
</html>
"""



COUNTDOWN_SCRIPT = r"""
<!-- Market Research 24-Hour Countdown Banner: Stripe Checkout, Responsive, No Overlap -->
<style>
  #cc360-banner {
    position: fixed;
    top: 0; left: 0; width: 100%;
    display: flex; flex-wrap: wrap; justify-content: center; align-items: center;
    background: #f0f8ff; color: #1e293b; font-size: 15px; z-index: 1000;
    box-shadow: 0 2px 8px rgba(30,41,59,0.07);
    padding: 12px 18px;
    gap: 1rem;
    min-height: 54px;
  }
  #cc360-count { font-weight: 700; letter-spacing: 1px; }
  #cc360-link {
    background: #3b82f6; color: #fff; border: none; border-radius: 5px;
    padding: 8px 20px; font-weight: 600; font-size: 15px; cursor: pointer;
    text-decoration: none; transition: background .18s;
    box-shadow: 0 1px 3px rgba(30,41,59,0.03);
  }
  #cc360-link:hover { background: #2563eb; }
  @media (max-width: 768px) {
    #cc360-banner {
      position: fixed;
      min-height: 32px;
      font-size: 11px;
      flex-direction: row;
      align-items: center;
      text-align: center;
      gap: 0.5rem;
      padding: 6px 12px;
    }
    #cc360-link {
      padding: 4px 12px;
      font-size: 11px;
    }
  }
</style>
<div id="cc360-banner">
  <span>
    Start your 30-day trial in the next 24 h for a free course + custom website.
  </span>
  <span>Time left: <span id="cc360-count">24:00:00</span></span>
  <a id="cc360-link" href="#" target="_blank" rel="noopener">Sign Up</a>
</div>
<script>
(async()=>{
  // Stripe settings
  const PUBLISHABLE_KEY  = "pk_live_51LNznbBnnqL8bKFQDpqXsQJ00WefQSSLMf2CZWr0sarinvaalkyY0BE7q7swLzIt49RSiCgBAP5uPHjU8fBNDsf0008MSXCQFU";
  const SESSION_ENDPOINT = "https://3k62eq3mjyecfujkgbmrophvwq0xigra.lambda-url.us-west-2.on.aws/";
  const FALLBACK_URL     = "https://checkout.coursecreator360.com/b/dR6cNB7Im6N85IA9AF";

  // Load Stripe.js
  await new Promise((ok,fail)=>{
    let s=document.createElement("script");
    s.src="https://js.stripe.com/v3/";
    s.onload=ok; s.onerror=()=>fail(Error("Stripe.js failed"));
    document.head.appendChild(s);
  });
  const stripe = Stripe(PUBLISHABLE_KEY);

  // Fetch Checkout session (if available)
  let sessionId = null;
  try {
    const qs = new URLSearchParams(location.search);
    const body = qs.get("ai_website_id") ? { ai_website_id: qs.get("ai_website_id") } : {};
    const res = await fetch(SESSION_ENDPOINT, {method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
    if(res.ok) sessionId = (await res.json()).clientSecret;
  } catch(e) { /* fallback below */ }

  // Open checkout in new tab (always)
  function openCheckout() {
    const checkoutUrl = sessionId
      ? `https://checkout.stripe.com/pay/${sessionId}`
      : FALLBACK_URL;
    window.open(checkoutUrl, "_blank", "noopener");
  }
  document.getElementById("cc360-link").onclick = e => { e.preventDefault(); openCheckout(); };

  // Countdown persistence (per-report)
  const id = new URLSearchParams(location.search).get("temp_market_research_id") || "default";
  const key = "countdown_expiry_" + id;
  let expiry = +localStorage.getItem(key) || (Date.now()+24*60*60*1000);
  localStorage.setItem(key, expiry);

  // Countdown UI & auto-redirect
  function tick() {
    const diff = expiry - Date.now();
    if(diff<=0){ openCheckout(); return; }
    const h=Math.floor(diff/36e5), m=Math.floor((diff%36e5)/6e4), s=Math.floor((diff%6e4)/1e3);
    document.getElementById("cc360-count").textContent = `${h.toString().padStart(2,0)}:${m.toString().padStart(2,0)}:${s.toString().padStart(2,0)}`;
  }
  tick(); setInterval(tick, 1000);

  // Desktop: push content down by banner height
  function updateBannerOffset(){
    const banner = document.getElementById("cc360-banner");
    if(window.matchMedia("(max-width:768px)").matches){
      document.documentElement.style.setProperty("--cc360-banner-height","0px");
    } else {
      document.documentElement.style.setProperty("--cc360-banner-height", banner.offsetHeight+"px");
    }
  }
  updateBannerOffset();
  window.addEventListener("resize",updateBannerOffset);
})();
</script>
"""
<template>
  <div class="home-container">
    <!-- Top Navigation Bar -->
    <nav class="navbar">
      <div class="nav-brand">MIROFISH</div>
      <div class="nav-links">
        <a href="#how-it-works" class="nav-link">How It Works</a>
        <a href="#best-practices" class="nav-link">Best Practices</a>
        <a href="#resources" class="nav-link">Resources</a>
        <a href="https://github.com/666ghj/MiroFish" target="_blank" class="github-link">
          GitHub <span class="arrow">&#8599;</span>
        </a>
      </div>
    </nav>

    <div class="main-content">
      <!-- Hero Section -->
      <section class="hero-section">
        <div class="hero-left">
          <div class="tag-row">
            <span class="accent-tag">Multi-Agent Simulation Engine</span>
            <span class="version-text">v0.1-Preview</span>
          </div>

          <h1 class="main-title">
            Upload Any Report.<br>
            <span class="gradient-text">Simulate the Future.</span>
          </h1>

          <div class="hero-desc">
            <p>
              <strong>MiroFish</strong> automatically generates a parallel world composed of up to
              <span class="highlight-accent">millions of Agents</span> from your real-world data.
              Inject variables, observe complex group interactions, and find
              <span class="highlight-code">"local optima"</span> in dynamic environments.
            </p>
            <p class="slogan-text">
              Let the future rehearse among Agents, let decisions prevail after a hundred battles<span class="blinking-cursor">_</span>
            </p>
          </div>
        </div>

        <div class="hero-right">
          <div class="logo-container">
            <img src="../assets/logo/MiroFish_logo_left.jpeg" alt="MiroFish Logo" class="hero-logo" />
          </div>
          <button class="scroll-down-btn" @click="scrollToBottom">&#8595;</button>
        </div>
      </section>

      <!-- Dashboard: Upload + Workflow -->
      <section class="dashboard-section">
        <!-- Left Column: Status & Steps -->
        <div class="left-panel">
          <div class="panel-header">
            <span class="status-dot">&#9632;</span> System Status
          </div>

          <h2 class="section-title">Ready</h2>
          <p class="section-desc">
            Prediction engine on standby. Upload unstructured data files to initialize a simulation sequence.
          </p>

          <!-- Metrics -->
          <div class="metrics-row">
            <div class="metric-card">
              <div class="metric-value">~$5</div>
              <div class="metric-label">Avg. cost per standard simulation run</div>
            </div>
            <div class="metric-card">
              <div class="metric-value">1M+</div>
              <div class="metric-label">Agents per simulation capacity</div>
            </div>
          </div>

          <!-- Workflow Steps -->
          <div class="steps-container" id="how-it-works">
            <div class="steps-header">
              <span class="diamond-icon">&#9671;</span> Workflow Sequence
            </div>
            <div class="workflow-list">
              <div class="workflow-item" v-for="(step, i) in workflowSteps" :key="i">
                <span class="step-num">{{ String(i + 1).padStart(2, '0') }}</span>
                <div class="step-info">
                  <div class="step-title">{{ step.title }}</div>
                  <div class="step-desc">{{ step.desc }}</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Interactive Console -->
        <div class="right-panel">
          <div class="console-box">
            <!-- Upload Area -->
            <div class="console-section">
              <div class="console-header">
                <span class="console-label">01 / Real-World Seeds</span>
                <span class="console-meta">PDF, MD, TXT</span>
              </div>

              <div
                class="upload-zone"
                :class="{ 'drag-over': isDragOver, 'has-files': files.length > 0 }"
                @dragover.prevent="handleDragOver"
                @dragleave.prevent="handleDragLeave"
                @drop.prevent="handleDrop"
                @click="triggerFileInput"
              >
                <input
                  ref="fileInput"
                  type="file"
                  multiple
                  accept=".pdf,.md,.txt"
                  @change="handleFileSelect"
                  style="display: none"
                  :disabled="loading"
                />

                <div v-if="files.length === 0" class="upload-placeholder">
                  <div class="upload-icon">&#8593;</div>
                  <div class="upload-title">Drag and drop files to upload</div>
                  <div class="upload-hint">or click to browse</div>
                </div>

                <div v-else class="file-list">
                  <div v-for="(file, index) in files" :key="index" class="file-item">
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">{{ file.name }}</span>
                    <button @click.stop="removeFile(index)" class="remove-btn">&times;</button>
                  </div>
                </div>
              </div>
            </div>

            <!-- Divider -->
            <div class="console-divider"><span>Input Parameters</span></div>

            <!-- Simulation Prompt -->
            <div class="console-section">
              <div class="console-header">
                <span class="console-label">>_ 02 / Simulation Prompt</span>
              </div>
              <div class="input-wrapper">
                <textarea
                  v-model="formData.simulationRequirement"
                  class="code-input"
                  placeholder="Enter your simulation requirement in natural language..."
                  rows="6"
                  :disabled="loading"
                ></textarea>
                <div class="model-badge">Engine: MiroFish-V1.0</div>
              </div>
            </div>

            <!-- Launch Button -->
            <div class="console-section btn-section">
              <button
                class="start-engine-btn"
                @click="startSimulation"
                :disabled="!canSubmit || loading"
              >
                <span v-if="!loading">Launch Engine</span>
                <span v-else>Initializing...</span>
                <span class="btn-arrow">&rarr;</span>
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- Known Constraints Section -->
      <section class="info-section" id="best-practices">
        <div class="info-header">
          <h2 class="info-title">Before You Start</h2>
          <p class="info-subtitle">Key constraints, best practices, and cost considerations for running effective simulations.</p>
        </div>

        <div class="info-grid">
          <!-- Known Constraints -->
          <div class="info-card">
            <div class="info-card-header">
              <span class="info-card-icon">!</span>
              <h3>Known Constraints</h3>
            </div>
            <ul class="info-list">
              <li><strong>File size limit:</strong> Each uploaded document should be under 10 MB. Larger files may time out during ontology extraction.</li>
              <li><strong>Language:</strong> Best results with English-language source material. Other languages may produce less accurate agent personas.</li>
              <li><strong>LLM dependency:</strong> Simulation quality depends on the underlying LLM (currently GPT-4 class). Outputs are probabilistic, not deterministic.</li>
              <li><strong>Agent count scaling:</strong> Simulations beyond 10,000 agents significantly increase cost and runtime. Start small and scale up.</li>
              <li><strong>No real-time data:</strong> Agents reason from your uploaded seed data only &mdash; they do not access live internet or APIs during simulation.</li>
            </ul>
          </div>

          <!-- Best Practices -->
          <div class="info-card">
            <div class="info-card-header">
              <span class="info-card-icon accent">&#10003;</span>
              <h3>Best Practices</h3>
            </div>
            <ul class="info-list">
              <li><strong>Provide rich seed data:</strong> The more context in your uploads (market reports, guest reviews, competitor analyses), the richer the simulation.</li>
              <li><strong>Be specific with prompts:</strong> Instead of "what will happen," ask "how would luxury travelers aged 35-55 respond to a 15% rate increase at a 5-star beachfront resort?"</li>
              <li><strong>Iterate in rounds:</strong> Run a small simulation first (fewer agents, shorter rounds) to validate your hypothesis before scaling up.</li>
              <li><strong>Combine data sources:</strong> Upload multiple documents &mdash; e.g., a TripAdvisor sentiment report alongside a pricing strategy PDF &mdash; for richer multi-perspective simulations.</li>
              <li><strong>Review the ontology graph:</strong> After Step 1 completes, inspect the generated graph. If key entities are missing, adjust your seed data and re-run.</li>
            </ul>
          </div>

          <!-- Cost Thinking -->
          <div class="info-card">
            <div class="info-card-header">
              <span class="info-card-icon warn">$</span>
              <h3>Understanding Costs</h3>
            </div>
            <ul class="info-list">
              <li><strong>LLM token usage:</strong> Each agent interaction consumes API tokens. A 100-agent, 10-round simulation uses approximately 500K&ndash;2M tokens.</li>
              <li><strong>Ballpark pricing:</strong> Simple scenarios (50 agents, 5 rounds) cost ~$2&ndash;5. Complex scenarios (1000+ agents, 20+ rounds) can reach $20&ndash;50+.</li>
              <li><strong>Ontology generation:</strong> The initial graph build typically costs $0.50&ndash;$2 depending on document volume.</li>
              <li><strong>Report generation:</strong> The final analysis report adds ~$1&ndash;3 in token costs.</li>
              <li><strong>Tip:</strong> Set a budget ceiling before launching. Use the Environment Setup step (Step 2) to cap simulation rounds and agent count.</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- AI Tools & Resources Section -->
      <section class="resources-section" id="resources">
        <div class="info-header">
          <h2 class="info-title">AI Tools &amp; Resources</h2>
          <p class="info-subtitle">Curated tools and platforms for digital marketing agencies in luxury hospitality.</p>
        </div>

        <div class="resources-grid">
          <!-- Content & Creative -->
          <div class="resource-category">
            <h3 class="resource-cat-title">Content &amp; Creative</h3>
            <div class="resource-links">
              <a href="https://openai.com/chatgpt" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">ChatGPT</span>
                <span class="resource-desc">AI copywriting, brainstorming, guest persona creation</span>
              </a>
              <a href="https://www.anthropic.com/claude" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Claude</span>
                <span class="resource-desc">Long-form content, analysis, strategic planning</span>
              </a>
              <a href="https://www.midjourney.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Midjourney</span>
                <span class="resource-desc">AI image generation for campaign visuals and mood boards</span>
              </a>
              <a href="https://www.jasper.ai" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Jasper AI</span>
                <span class="resource-desc">Marketing-specific AI content platform with brand voice</span>
              </a>
            </div>
          </div>

          <!-- Analytics & Insights -->
          <div class="resource-category">
            <h3 class="resource-cat-title">Analytics &amp; Insights</h3>
            <div class="resource-links">
              <a href="https://analytics.google.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Google Analytics 4</span>
                <span class="resource-desc">Web analytics, audience insights, conversion tracking</span>
              </a>
              <a href="https://www.semrush.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">SEMrush</span>
                <span class="resource-desc">SEO, competitive analysis, keyword research for hospitality</span>
              </a>
              <a href="https://www.revinate.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Revinate</span>
                <span class="resource-desc">Hotel guest data platform, reputation management</span>
              </a>
              <a href="https://www.medallia.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Medallia</span>
                <span class="resource-desc">Experience management, guest feedback analysis at scale</span>
              </a>
            </div>
          </div>

          <!-- Automation & Campaigns -->
          <div class="resource-category">
            <h3 class="resource-cat-title">Automation &amp; Campaigns</h3>
            <div class="resource-links">
              <a href="https://www.hubspot.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">HubSpot</span>
                <span class="resource-desc">CRM, marketing automation, email campaigns</span>
              </a>
              <a href="https://www.cendyn.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Cendyn</span>
                <span class="resource-desc">Hospitality-specific CRM and digital marketing</span>
              </a>
              <a href="https://zapier.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Zapier</span>
                <span class="resource-desc">Workflow automation connecting 5000+ marketing tools</span>
              </a>
              <a href="https://www.sojern.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Sojern</span>
                <span class="resource-desc">Travel-specific programmatic advertising platform</span>
              </a>
            </div>
          </div>

          <!-- AI Strategy & Learning -->
          <div class="resource-category">
            <h3 class="resource-cat-title">AI Strategy &amp; Learning</h3>
            <div class="resource-links">
              <a href="https://www.phocuswire.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">PhocusWire</span>
                <span class="resource-desc">Travel technology and innovation news</span>
              </a>
              <a href="https://skift.com" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Skift</span>
                <span class="resource-desc">Travel industry intelligence and research</span>
              </a>
              <a href="https://www.hospitalitynet.org" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">Hospitality Net</span>
                <span class="resource-desc">Hotel industry technology trends and case studies</span>
              </a>
              <a href="https://www.mckinsey.com/industries/travel-logistics-and-infrastructure" target="_blank" rel="noopener" class="resource-link">
                <span class="resource-name">McKinsey Travel</span>
                <span class="resource-desc">Strategic insights on luxury travel and hospitality</span>
              </a>
            </div>
          </div>
        </div>
      </section>

      <!-- History -->
      <HistoryDatabase />

      <!-- Footer -->
      <footer class="site-footer">
        <div class="footer-content">
          <span class="footer-brand">MIROFISH</span>
          <span class="footer-sep">|</span>
          <span class="footer-text">Multi-Agent Social Simulation Engine</span>
        </div>
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import HistoryDatabase from '../components/HistoryDatabase.vue'

const router = useRouter()

// Workflow steps data
const workflowSteps = [
  { title: 'Graph Construction', desc: 'Real-world seed extraction, individual/group memory injection, and GraphRAG construction' },
  { title: 'Environment Setup', desc: 'Entity-relation extraction, persona generation, and environment configuration' },
  { title: 'Start Simulation', desc: 'Dual-platform parallel simulation with dynamic temporal memory updates' },
  { title: 'Report Generation', desc: 'ReportAgent uses a rich toolset to deeply analyze the post-simulation environment' },
  { title: 'Deep Interaction', desc: 'Chat with any individual in the simulated world or converse with ReportAgent' }
]

// Form data
const formData = ref({
  simulationRequirement: ''
})

// File list
const files = ref([])

// State
const loading = ref(false)
const error = ref('')
const isDragOver = ref(false)

// File input reference
const fileInput = ref(null)

// Computed property: whether submission is allowed
const canSubmit = computed(() => {
  return formData.value.simulationRequirement.trim() !== '' && files.value.length > 0
})

// Trigger file selection
const triggerFileInput = () => {
  if (!loading.value) {
    fileInput.value?.click()
  }
}

// Handle file selection
const handleFileSelect = (event) => {
  const selectedFiles = Array.from(event.target.files)
  addFiles(selectedFiles)
}

// Handle drag events
const handleDragOver = () => {
  if (!loading.value) {
    isDragOver.value = true
  }
}

const handleDragLeave = () => {
  isDragOver.value = false
}

const handleDrop = (e) => {
  isDragOver.value = false
  if (loading.value) return
  const droppedFiles = Array.from(e.dataTransfer.files)
  addFiles(droppedFiles)
}

// Add files
const addFiles = (newFiles) => {
  const validFiles = newFiles.filter(file => {
    const ext = file.name.split('.').pop().toLowerCase()
    return ['pdf', 'md', 'txt'].includes(ext)
  })
  files.value.push(...validFiles)
}

// Remove file
const removeFile = (index) => {
  files.value.splice(index, 1)
}

// Scroll to bottom
const scrollToBottom = () => {
  window.scrollTo({
    top: document.body.scrollHeight,
    behavior: 'smooth'
  })
}

// Start simulation
const startSimulation = () => {
  if (!canSubmit.value || loading.value) return
  import('../store/pendingUpload.js').then(({ setPendingUpload }) => {
    setPendingUpload(files.value, formData.value.simulationRequirement)
    router.push({
      name: 'Process',
      params: { projectId: 'new' }
    })
  })
}
</script>

<style scoped>
/* ===== VERB Interactive Brand Palette ===== */
:root {
  --verb-black: #0A0A0A;
  --verb-dark: #1A1A2E;
  --verb-white: #FFFFFF;
  --verb-cyan: #0693E3;
  --verb-cyan-light: #4DB8FF;
  --verb-orange: #FF6900;
  --verb-gray-100: #F7F8FA;
  --verb-gray-200: #E8EBF0;
  --verb-gray-300: #C8CDD5;
  --verb-gray-500: #6B7280;
  --verb-gray-700: #374151;
  --verb-purple: #9B51E0;
  --font-mono: 'JetBrains Mono', monospace;
  --font-sans: 'Inter', 'Space Grotesk', 'Noto Sans SC', system-ui, sans-serif;
}

.home-container {
  min-height: 100vh;
  background: var(--verb-white);
  font-family: var(--font-sans);
  color: var(--verb-black);
}

/* ===== Navbar ===== */
.navbar {
  height: 64px;
  background: var(--verb-black);
  color: var(--verb-white);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-brand {
  font-family: var(--font-mono);
  font-weight: 800;
  letter-spacing: 2px;
  font-size: 1.2rem;
  color: var(--verb-cyan);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 28px;
}

.nav-link {
  color: var(--verb-gray-300);
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 500;
  letter-spacing: 0.3px;
  transition: color 0.2s;
}

.nav-link:hover {
  color: var(--verb-white);
}

.github-link {
  color: var(--verb-white);
  text-decoration: none;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.08);
  padding: 6px 14px;
  border: 1px solid rgba(255, 255, 255, 0.15);
  transition: all 0.2s;
}

.github-link:hover {
  background: rgba(255, 255, 255, 0.15);
  border-color: var(--verb-cyan);
}

.arrow {
  font-family: sans-serif;
}

/* ===== Main Content ===== */
.main-content {
  max-width: 1320px;
  margin: 0 auto;
  padding: 56px 40px 0;
}

/* ===== Hero Section ===== */
.hero-section {
  display: flex;
  justify-content: space-between;
  margin-bottom: 72px;
  position: relative;
}

.hero-left {
  flex: 1;
  padding-right: 60px;
}

.tag-row {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 24px;
  font-family: var(--font-mono);
  font-size: 0.78rem;
}

.accent-tag {
  background: var(--verb-cyan);
  color: var(--verb-white);
  padding: 5px 12px;
  font-weight: 700;
  letter-spacing: 0.5px;
  font-size: 0.72rem;
  text-transform: uppercase;
}

.version-text {
  color: var(--verb-gray-500);
  font-weight: 500;
  letter-spacing: 0.5px;
}

.main-title {
  font-size: 3.8rem;
  line-height: 1.15;
  font-weight: 700;
  margin: 0 0 36px 0;
  letter-spacing: -1.5px;
  color: var(--verb-black);
}

.gradient-text {
  background: linear-gradient(135deg, var(--verb-cyan) 0%, var(--verb-purple) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}

.hero-desc {
  font-size: 1.02rem;
  line-height: 1.8;
  color: var(--verb-gray-500);
  max-width: 620px;
  margin-bottom: 40px;
  font-weight: 400;
}

.hero-desc p {
  margin-bottom: 1.2rem;
}

.hero-desc strong {
  color: var(--verb-black);
  font-weight: 700;
}

.highlight-accent {
  color: var(--verb-cyan);
  font-weight: 700;
  font-family: var(--font-mono);
}

.highlight-code {
  background: var(--verb-gray-100);
  padding: 2px 8px;
  font-family: var(--font-mono);
  font-size: 0.88em;
  color: var(--verb-black);
  font-weight: 600;
  border: 1px solid var(--verb-gray-200);
}

.slogan-text {
  font-size: 1.1rem;
  font-weight: 520;
  color: var(--verb-black);
  letter-spacing: 0.5px;
  border-left: 3px solid var(--verb-cyan);
  padding-left: 16px;
  margin-top: 16px;
}

.blinking-cursor {
  color: var(--verb-cyan);
  animation: blink 1s step-end infinite;
  font-weight: 700;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

.hero-right {
  flex: 0.75;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;
}

.logo-container {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  padding-right: 20px;
}

.hero-logo {
  max-width: 440px;
  width: 100%;
  border-radius: 4px;
}

.scroll-down-btn {
  width: 40px;
  height: 40px;
  border: 1px solid var(--verb-gray-200);
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--verb-cyan);
  font-size: 1.2rem;
  transition: all 0.2s;
}

.scroll-down-btn:hover {
  border-color: var(--verb-cyan);
  background: var(--verb-gray-100);
}

/* ===== Dashboard Section ===== */
.dashboard-section {
  display: flex;
  gap: 56px;
  border-top: 1px solid var(--verb-gray-200);
  padding-top: 56px;
  align-items: flex-start;
}

.left-panel {
  flex: 0.8;
}

.panel-header {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--verb-gray-500);
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 18px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.status-dot {
  color: var(--verb-cyan);
  font-size: 0.7rem;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  margin: 0 0 12px 0;
  color: var(--verb-black);
}

.section-desc {
  color: var(--verb-gray-500);
  margin-bottom: 24px;
  line-height: 1.6;
  font-size: 0.95rem;
}

.metrics-row {
  display: flex;
  gap: 16px;
  margin-bottom: 20px;
}

.metric-card {
  border: 1px solid var(--verb-gray-200);
  padding: 20px 28px;
  min-width: 140px;
  background: var(--verb-gray-100);
}

.metric-value {
  font-family: var(--font-mono);
  font-size: 1.6rem;
  font-weight: 700;
  margin-bottom: 4px;
  color: var(--verb-cyan);
}

.metric-label {
  font-size: 0.82rem;
  color: var(--verb-gray-500);
}

/* Workflow Steps */
.steps-container {
  border: 1px solid var(--verb-gray-200);
  padding: 28px;
  background: var(--verb-gray-100);
}

.steps-header {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--verb-gray-500);
  margin-bottom: 22px;
  display: flex;
  align-items: center;
  gap: 8px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.diamond-icon {
  font-size: 1.1rem;
  color: var(--verb-cyan);
}

.workflow-list {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.workflow-item {
  display: flex;
  align-items: flex-start;
  gap: 18px;
}

.step-num {
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--verb-cyan);
  opacity: 0.5;
  font-size: 0.9rem;
  min-width: 24px;
}

.step-info {
  flex: 1;
}

.step-title {
  font-weight: 600;
  font-size: 0.95rem;
  margin-bottom: 3px;
  color: var(--verb-black);
}

.step-desc {
  font-size: 0.82rem;
  color: var(--verb-gray-500);
  line-height: 1.5;
}

/* ===== Right Console ===== */
.right-panel {
  flex: 1.2;
}

.console-box {
  border: 2px solid var(--verb-black);
  padding: 6px;
  background: var(--verb-white);
}

.console-section {
  padding: 18px;
}

.console-section.btn-section {
  padding-top: 0;
}

.console-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 12px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--verb-gray-500);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.upload-zone {
  border: 1px dashed var(--verb-gray-300);
  height: 190px;
  overflow-y: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
  background: var(--verb-gray-100);
}

.upload-zone.has-files {
  align-items: flex-start;
}

.upload-zone:hover {
  background: var(--verb-gray-200);
  border-color: var(--verb-cyan);
}

.upload-zone.drag-over {
  border-color: var(--verb-cyan);
  background: rgba(6, 147, 227, 0.05);
}

.upload-placeholder {
  text-align: center;
}

.upload-icon {
  width: 40px;
  height: 40px;
  border: 1px solid var(--verb-gray-300);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 12px;
  color: var(--verb-cyan);
  font-size: 1.1rem;
}

.upload-title {
  font-weight: 500;
  font-size: 0.88rem;
  margin-bottom: 4px;
  color: var(--verb-gray-700);
}

.upload-hint {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--verb-gray-500);
}

.file-list {
  width: 100%;
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.file-item {
  display: flex;
  align-items: center;
  background: var(--verb-white);
  padding: 8px 12px;
  border: 1px solid var(--verb-gray-200);
  font-family: var(--font-mono);
  font-size: 0.82rem;
}

.file-name {
  flex: 1;
  margin: 0 10px;
}

.remove-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
  color: var(--verb-gray-500);
  transition: color 0.2s;
}

.remove-btn:hover {
  color: #E53E3E;
}

.console-divider {
  display: flex;
  align-items: center;
  margin: 8px 0;
}

.console-divider::before,
.console-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--verb-gray-200);
}

.console-divider span {
  padding: 0 14px;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: var(--verb-gray-300);
  letter-spacing: 1px;
  text-transform: uppercase;
}

.input-wrapper {
  position: relative;
  border: 1px solid var(--verb-gray-200);
  background: var(--verb-gray-100);
}

.code-input {
  width: 100%;
  border: none;
  background: transparent;
  padding: 18px;
  font-family: var(--font-mono);
  font-size: 0.88rem;
  line-height: 1.6;
  resize: vertical;
  outline: none;
  min-height: 140px;
  color: var(--verb-black);
}

.code-input::placeholder {
  color: var(--verb-gray-300);
}

.model-badge {
  position: absolute;
  bottom: 10px;
  right: 14px;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: var(--verb-gray-300);
}

.start-engine-btn {
  width: 100%;
  background: var(--verb-black);
  color: var(--verb-white);
  border: none;
  padding: 18px;
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: all 0.2s;
  letter-spacing: 1px;
}

.start-engine-btn:not(:disabled) {
  background: var(--verb-black);
}

.start-engine-btn:hover:not(:disabled) {
  background: var(--verb-cyan);
}

.start-engine-btn:disabled {
  background: var(--verb-gray-200);
  color: var(--verb-gray-500);
  cursor: not-allowed;
}

/* ===== Info Section: Constraints, Best Practices, Costs ===== */
.info-section {
  margin-top: 80px;
  padding-top: 56px;
  border-top: 1px solid var(--verb-gray-200);
}

.info-header {
  text-align: center;
  margin-bottom: 48px;
}

.info-title {
  font-size: 2.2rem;
  font-weight: 700;
  color: var(--verb-black);
  margin: 0 0 10px 0;
  letter-spacing: -0.5px;
}

.info-subtitle {
  color: var(--verb-gray-500);
  font-size: 1rem;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
}

.info-card {
  background: var(--verb-gray-100);
  border: 1px solid var(--verb-gray-200);
  padding: 32px 28px;
}

.info-card-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--verb-gray-200);
}

.info-card-header h3 {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--verb-black);
  margin: 0;
}

.info-card-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-weight: 800;
  font-size: 0.85rem;
  background: var(--verb-black);
  color: var(--verb-white);
  flex-shrink: 0;
}

.info-card-icon.accent {
  background: var(--verb-cyan);
}

.info-card-icon.warn {
  background: var(--verb-orange);
}

.info-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.info-list li {
  font-size: 0.88rem;
  line-height: 1.6;
  color: var(--verb-gray-700);
  padding-left: 14px;
  position: relative;
}

.info-list li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  width: 4px;
  height: 4px;
  background: var(--verb-cyan);
}

.info-list li strong {
  color: var(--verb-black);
  font-weight: 600;
}

/* ===== Resources Section ===== */
.resources-section {
  margin-top: 80px;
  padding-top: 56px;
  border-top: 1px solid var(--verb-gray-200);
}

.resources-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
}

.resource-category {
  background: var(--verb-gray-100);
  border: 1px solid var(--verb-gray-200);
  padding: 28px;
}

.resource-cat-title {
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: var(--verb-cyan);
  margin: 0 0 18px 0;
  font-family: var(--font-mono);
  padding-bottom: 12px;
  border-bottom: 1px solid var(--verb-gray-200);
}

.resource-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.resource-link {
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: 12px 16px;
  background: var(--verb-white);
  border: 1px solid var(--verb-gray-200);
  text-decoration: none;
  transition: all 0.2s;
}

.resource-link:hover {
  border-color: var(--verb-cyan);
  transform: translateX(4px);
}

.resource-name {
  font-weight: 600;
  font-size: 0.92rem;
  color: var(--verb-black);
}

.resource-desc {
  font-size: 0.78rem;
  color: var(--verb-gray-500);
  line-height: 1.4;
}

/* ===== Footer ===== */
.site-footer {
  margin-top: 80px;
  padding: 32px 0;
  border-top: 1px solid var(--verb-gray-200);
  text-align: center;
}

.footer-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  font-size: 0.82rem;
  color: var(--verb-gray-500);
}

.footer-brand {
  font-family: var(--font-mono);
  font-weight: 800;
  letter-spacing: 2px;
  color: var(--verb-black);
}

.footer-sep {
  color: var(--verb-gray-300);
}

/* ===== Responsive ===== */
@media (max-width: 1024px) {
  .dashboard-section {
    flex-direction: column;
  }

  .hero-section {
    flex-direction: column;
  }

  .hero-left {
    padding-right: 0;
    margin-bottom: 40px;
  }

  .hero-logo {
    max-width: 240px;
    margin-bottom: 20px;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }

  .resources-grid {
    grid-template-columns: 1fr;
  }

  .main-title {
    font-size: 2.6rem;
  }

  .nav-links .nav-link {
    display: none;
  }
}
</style>

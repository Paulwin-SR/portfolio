const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  const htmlContent = fs.readFileSync('resume_temp.html', 'utf8');
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setContent(htmlContent, { waitUntil: 'networkidle0' });
  await page.pdf({ path: 'public/PAULWIN_S_R_Resume.pdf', format: 'A4', printBackground: true });
  await browser.close();
  console.log("PDF generated.");
})();

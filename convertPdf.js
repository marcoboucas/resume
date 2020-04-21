const puppeteer = require('puppeteer')
const fs = require('fs');

async function printPDF() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('http://localhost:5500/cv.html', {waitUntil: 'networkidle0'});
  const pdf = await page.pdf({ 
    format: 'A4',
    printBackground: true
  });
 
  await browser.close();
  return pdf
}
printPDF().then((buffer, err)=>{
  if (err) console.log(err)
  fs.writeFile("./public/cv.pdf", buffer, (err)=>{
    console.log(err)
  })
})
const puppeteer = require('puppeteer')
const fs = require('fs');


async function printPDF(PORT) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(`http://localhost:${PORT}/cv.html`, {waitUntil: 'networkidle0'});
  const pdf = await page.pdf({ 
    format: 'A4',
    printBackground: true
  });
 
  await browser.close();
  return pdf
}


const express = require('express')
const app = express()

const PORT = 3000
app.get('', function (req, res) {
  res.redirect('/cv.pdf')
})

app.use(express.static('public'));


app.listen(PORT, function () {
  console.log(`Example app listening on port ${PORT}!`)

  
  printPDF(PORT).then((buffer, err)=>{
    if (err) console.log(err)
    fs.writeFile("./public/cv.pdf", buffer, (err)=>{
      console.log(err)
    })
  })

})
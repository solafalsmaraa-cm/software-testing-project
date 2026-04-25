const { test, expect } = require('@playwright/test');

test('Real User Scenario: Add two numbers via UI and verify result', async ({ page }) => {
  // 1. فتح الصفحة الرئيسية
  await page.goto('/');

  // 2. إدخال الرقم الأول والثاني
  await page.fill('#num1', '15');
  await page.fill('#num2', '25');

  // 3. الضغط على زر الإضافة
  await page.click('#addBtn'); 

  // 4. التحقق من ظهور النتيجة الصحيحة (40)
  await expect(page.locator('#resultDisplay')).toHaveText('40');
});
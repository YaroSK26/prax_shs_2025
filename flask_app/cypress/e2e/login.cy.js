describe('Login and navigate to app', () => {
  const username = 'student'; // Nahraď hodnotou USERNAME_APP z .env
  const password = "prax2025"; // Nahraď hodnotou PASSWORD z .env

  it('Logs in and navigates to the app', () => {
    // Otvorí login stránku
    cy.visit("http://127.0.0.1:5000");

    // Vyplní prihlasovacie údaje
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(password);

    // Klikne na tlačidlo Login
    cy.get('button[type="submit"]').click();

    // Overí presmerovanie na /homepage
    cy.url().should('include', '/homepage');

    // Klikne na odkaz "Go to App"
    cy.contains('a', 'Go to App').click();

    // Overí presmerovanie na /app
    cy.url().should('include', '/app');

    // Overí, že stránka obsahuje text "App Page"
    cy.contains('h1', 'App Page').should('be.visible');
  });
});
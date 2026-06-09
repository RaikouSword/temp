#include <SFML/Graphics.hpp>
#include "Player.cpp"
#include "Zombie.cpp"
#include <iostream>

using namespace sf;
int createBackground(VertexArray &rVA, IntRect arena);
Zombie *createHorde(int numZombies, IntRect arena);
int main()
{
    Vector2f resolution;
    resolution.x = VideoMode::getDesktopMode().width;
    resolution.y = VideoMode::getDesktopMode().height;

    RenderWindow window(VideoMode(resolution.x, resolution.y),
                        "Zombie Arena", Style::Fullscreen);

    View mainView(sf::FloatRect(0, 0, resolution.x, resolution.y));
    Clock clock;
    Vector2f mouseWorldPosition;
    Vector2i mouseScreenPosition;
    Player player;
    IntRect arena;
    // Create the background
    VertexArray background;
    // Load the texture for our background vertex array
    Texture textureBackground;
    textureBackground.loadFromFile("graphics/background_sheet.png");

    arena.width = 500;
    arena.height = 500;
    arena.left = 0;
    arena.top = 0;
    // int tileSize = 50;
    int wave = 1;
    int tileSize = createBackground(background, arena);
    std::cout << tileSize << std::endl;
    player.spawn(arena, resolution, tileSize);
    int numZombies = wave * 2;
    Zombie *zombies = createHorde(numZombies, arena);

    int numZombiesAlive = numZombies;
    RectangleShape rect;
    Time dt;

    // indow.setView(mainView);
    while (window.isOpen())
    {
        Event event;
        while (window.pollEvent(event))
        {
            if (event.type == Event::Closed)
                window.close();
        } // End event polling

        if (Keyboard::isKeyPressed(Keyboard::Escape))
        {
            window.close();
        }

        if (Keyboard::isKeyPressed(Keyboard::W))
        {
            player.moveUp();
            std::cout << "W Pressed\n";
            std::cout << "Player X: " << player.getCenter().x << " Player Y: " << player.getCenter().y << std::endl;
        }
        else
        {
            player.stopUp();
            // std::cout<<"W Released\n";
        }

        if (Keyboard::isKeyPressed(Keyboard::S))
        {
            player.moveDown();
        }
        else
        {
            player.stopDown();
        }

        if (Keyboard::isKeyPressed(Keyboard::A))
        {
            player.moveLeft();
        }
        else
        {
            player.stopLeft();
        }

        if (Keyboard::isKeyPressed(Keyboard::D))
        {
            player.moveRight();
        }
        else
        {
            player.stopRight();
        }

        rect.setPosition(Vector2f(arena.top, arena.left));
        rect.setSize(Vector2f(arena.width, arena.height));
        rect.setFillColor(Color::Blue);

        dt = clock.restart();
        float dtAsSeconds = dt.asSeconds();

        player.update(dtAsSeconds, Mouse::getPosition());
        // Vector2f playerPosition
        for (int i = 0; i < numZombies; i++)
        {
            zombies[i].update(dtAsSeconds,player.getCenter());
        }

        mainView.setCenter(player.getCenter());
        // for(int i=0;i<numZombies;i++){
        //     	zombies[i].update(dtAsSeconds,playerPosition);

        // }
        // mainView.setCenter(Vector2f(arena.width / 2.0f, arena.height / 2.0f));
        window.clear(Color::Red);

        // set the mainView to be displayed in the window
        // And draw everything related to it
        window.setView(mainView);
        // Draw the background
        // window.draw(background, &textureBackground);

        // Draw the player
        window.draw(rect);

        // Draw the background
        window.draw(background, &textureBackground);
        // window.draw(textureBackground);
        window.draw(player.getSprite());
        for (int i = 0; i < numZombies; i++)
        {
            window.draw(zombies[i].getSprite());
        }
        window.display();

    } // End game loop

    return 0;
}

int createBackground(VertexArray &rVA, IntRect arena)
{
    // Anything we do to rVA we are actually doing to background (in the main function)

    // How big is each tile/texture
    const int TILE_SIZE = 50;
    const int TILE_TYPES = 3;
    const int VERTS_IN_QUAD = 4;

    int worldWidth = arena.width / TILE_SIZE;
    int worldHeight = arena.height / TILE_SIZE;

    // What type of primitive are we using?
    rVA.setPrimitiveType(Quads);

    // Set the size of the vertex array
    rVA.resize(worldWidth * worldHeight * VERTS_IN_QUAD);

    // Start at the beginning of the vertex array
    int currentVertex = 0;
    for (int w = 0; w < worldWidth; w++)
    {
        for (int h = 0; h < worldHeight; h++)
        {
            // Position each vertex in the current quad
            rVA[currentVertex + 0].position = Vector2f(w * TILE_SIZE, h * TILE_SIZE);
            rVA[currentVertex + 1].position = Vector2f((w * TILE_SIZE) + TILE_SIZE, h * TILE_SIZE);
            rVA[currentVertex + 2].position = Vector2f((w * TILE_SIZE) + TILE_SIZE, (h * TILE_SIZE) + TILE_SIZE);
            rVA[currentVertex + 3].position = Vector2f((w * TILE_SIZE), (h * TILE_SIZE) + TILE_SIZE);

            // Define the position in the Texture to draw for current quad
            // Either mud, stone, grass or wall
            if (h == 0 || h == worldHeight - 1 || w == 0 || w == worldWidth - 1)
            {
                // Use the wall texture
                rVA[currentVertex + 0].texCoords = Vector2f(0, 0 + TILE_TYPES * TILE_SIZE);
                rVA[currentVertex + 1].texCoords = Vector2f(TILE_SIZE, 0 + TILE_TYPES * TILE_SIZE);
                rVA[currentVertex + 2].texCoords = Vector2f(TILE_SIZE, TILE_SIZE + TILE_TYPES * TILE_SIZE);
                rVA[currentVertex + 3].texCoords = Vector2f(0, TILE_SIZE + TILE_TYPES * TILE_SIZE);
            }
            else
            {
                // Use a random floor texture
                srand((int)time(0) + h * w - h);
                int mOrG = (rand() % TILE_TYPES);
                int verticalOffset = mOrG * TILE_SIZE;

                rVA[currentVertex + 0].texCoords = Vector2f(0, 0 + verticalOffset);
                rVA[currentVertex + 1].texCoords = Vector2f(TILE_SIZE, 0 + verticalOffset);
                rVA[currentVertex + 2].texCoords = Vector2f(TILE_SIZE, TILE_SIZE + verticalOffset);
                rVA[currentVertex + 3].texCoords = Vector2f(0, TILE_SIZE + verticalOffset);
            }

            // Position ready for the next for vertices
            currentVertex = currentVertex + VERTS_IN_QUAD;
        }
    }

    return TILE_SIZE;
}

Zombie *createHorde(int numZombies, IntRect arena)
{
    Zombie *zombies = new Zombie[numZombies];
    int maxX = arena.width - 20;
    int minX = arena.left + 20;
    int maxY = arena.height - 20;
    int minY = arena.top + 20;

    for (int i = 0; i < numZombies; i++)
    {
        srand((int)time(0) * i);
        int side = (rand() % 4);
        float x, y;
        switch (side)
        {
        case 0:
            x = minX;
            y = (rand() % maxY) + minY;
            break;
        case 1:
            x = maxX;
            y = (rand() % maxY) + minY;
            break;
        case 2:
            y = minY;
            x = (rand() % maxX) + minX;
            break;
        case 3:
            y = maxY;
            x = (rand() % maxX) + minX;
            break;
        }
        srand((int)time(0) * i * 2);
        int type = (rand() % 3);
        zombies[i].spawn(x, y, type, i);
    }
    return zombies;
}

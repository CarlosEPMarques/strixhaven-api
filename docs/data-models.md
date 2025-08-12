# Data Model

## Enumerations

### `user_role`

* Possible values: `'DM'`, `'PLAYER'`

---

## Tables

### `users`

| Column      | Type         | Constraints                     | Description                |
| ----------- | ------------ | ------------------------------- | -------------------------- |
| id          | UUID         | PK                              | Unique user identifier     |
| name        | VARCHAR(100) | NOT NULL                        | User's name                |
| email       | VARCHAR(100) | UNIQUE, NOT NULL                | User's email               |
| password    | VARCHAR(255) | NOT NULL                        | User's password            |
| role        | `user_role`  | NOT NULL                        | User's role (DM or PLAYER) |
| avatar\_url | TEXT         |                                 | URL to user's avatar image |

---

### `colleges`

| Column      | Type         | Constraints                     | Description          |
| ----------- | ------------ | ------------------------------- | -------------------- |
| id          | UUID         | PK                              | College identifier   |
| name        | VARCHAR(255) | NOT NULL                        | College name         |
| description | TEXT         |                                 | College description  |
| image\_url  | TEXT         |                                 | URL to college image |

---

### `classes`

| Column      | Type         | Constraints                              | Description        |
| ----------- | ------------ | ---------------------------------------- | ------------------ |
| id          | UUID         | PK                                       | Class identifier   |
| name        | VARCHAR(255) | NOT NULL                                 | Class name         |
| description | TEXT         |                                          | Class description  |
| college\_id | UUID         | FK to `colleges(id)`, ON DELETE SET NULL | Associated college |
| image\_url  | TEXT         |                                          | URL to class image |

---

### `player_characters`

| Column            | Type         | Constraints                              | Description            |
| ----------------- | ------------ | ---------------------------------------- | ---------------------- |
| id                | UUID         | PK                                       | Character identifier   |
| user\_id          | UUID         | FK to `users(id)`, ON DELETE CASCADE     | Owning user            |
| name              | VARCHAR(255) | NOT NULL                                 | Character name         |
| image\_url        | TEXT         |                                          | URL to character image |
| college\_year     | INT          |                                          | College year           |
| college\_id       | UUID         | FK to `colleges(id)`, ON DELETE SET NULL | Character's college    |
| enrolled\_classes | TEXT         |                                          | Enrolled classes       |
| level             | INT          |                                          | Character level        |

---

### `inventory_items`

| Column        | Type  | Constraints                                      | Description               |
| ------------- | ----- | ------------------------------------------------ | ------------------------- |
| id            | UUID  | PK                                               | Inventory item identifier |
| character\_id | UUID  | FK to `player_characters(id)`, ON DELETE CASCADE | Owner character           |
| item\_id      | UUID  |                                                  | Item identifier           |
| amount        | INT   |                                                  | Quantity                  |
| metadata      | JSONB |                                                  | Additional metadata       |

---

### `character_sheet`

| Column               | Type      | Constraints                                      | Description                |
| -------------------- | --------- | ------------------------------------------------ | -------------------------- |
| id                   | UUID      | PK                                               | Character sheet identifier |
| character\_id        | UUID      | FK to `player_characters(id)`, ON DELETE CASCADE | Associated character       |
| strength             | INTEGER   |                                                  | Strength                   |
| dexterity            | INTEGER   |                                                  | Dexterity                  |
| constitution         | INTEGER   |                                                  | Constitution               |
| intelligence         | INTEGER   |                                                  | Intelligence               |
| wisdom               | INTEGER   |                                                  | Wisdom                     |
| charisma             | INTEGER   |                                                  | Charisma                   |
| proficiency\_bonus   | INTEGER   |                                                  | Proficiency bonus          |
| armor\_class         | INTEGER   |                                                  | Armor class                |
| initiative           | INTEGER   |                                                  | Initiative                 |
| speed                | FLOAT     |                                                  | Movement speed             |
| max\_hit\_points     | INTEGER   |                                                  | Maximum hit points         |
| current\_hit\_points | INTEGER   |                                                  | Current hit points         |
| temp\_hit\_points    | INTEGER   |                                                  | Temporary hit points       |
| hit\_dice\_total     | INTEGER   |                                                  | Total hit dice             |
| hit\_dice\_current   | INTEGER   |                                                  | Current hit dice           |
| save\_str            | INTEGER   |                                                  | Strength saving throw      |
| save\_dex            | INTEGER   |                                                  | Dexterity saving throw     |
| save\_con            | INTEGER   |                                                  | Constitution saving throw  |
| save\_int            | INTEGER   |                                                  | Intelligence saving throw  |
| save\_wis            | INTEGER   |                                                  | Wisdom saving throw        |
| save\_cha            | INTEGER   |                                                  | Charisma saving throw      |
| skills               | TEXT      |                                                  | Skills                     |
| background           | TEXT      |                                                  | Background                 |
| race                 | TEXT      |                                                  | Race                       |
| alignment            | TEXT      |                                                  | Alignment                  |
| experience\_points   | INTEGER   |                                                  | Experience points          |
| languages            | TEXT      |                                                  | Languages                  |
| features\_traits     | TEXT      |                                                  | Features and traits        |
| proficiencies        | TEXT      |                                                  | Proficiencies              |
| description          | TEXT      |                                                  | Description                |
| created\_at          | TIMESTAMP | Default NOW()                                    | Creation timestamp         |
| updated\_at          | TIMESTAMP | Default NOW()                                    | Update timestamp           |

---

### `npcs`

| Column      | Type         | Constraints                     | Description         |
| ----------- | ------------ | ------------------------------- | ------------------- |
| id          | UUID         | PK                              | NPC identifier      |
| name        | VARCHAR(255) | NOT NULL                        | NPC name            |
| image\_url  | TEXT         |                                 | NPC image URL       |
| bio         | TEXT         |                                 | NPC biography       |
| is\_visible | BOOLEAN      | Default TRUE                    | Visibility flag     |
| visible\_to | TEXT         |                                 | Specific visibility |

---

### `npcs_reputation`

| Column        | Type | Constraints                                      | Description                  |
| ------------- | ---- | ------------------------------------------------ | ---------------------------- |
| id            | UUID | PK                                               | Reputation record identifier |
| character\_id | UUID | FK to `player_characters(id)`, ON DELETE CASCADE | Character                    |
| npc\_id       | UUID | FK to `npcs(id)`, ON DELETE CASCADE              | NPC                          |
| score         | INT  |                                                  | Reputation score             |

---

### `notes`

| Column           | Type      | Constraints                          | Description        |
| ---------------- | --------- | ------------------------------------ | ------------------ |
| id               | UUID      | PK                                   | Note identifier    |
| author\_id       | UUID      | FK to `users(id)`, ON DELETE CASCADE | Note author        |
| content          | TEXT      | NOT NULL                             | Note content       |
| is\_master\_only | BOOLEAN   | Default FALSE                        | Master-only flag   |
| is\_privative    | BOOLEAN   | Default FALSE                        | Private note flag  |
| created\_at      | TIMESTAMP | Default NOW()                        | Creation timestamp |
| updated\_at      | TIMESTAMP | Default NOW()                        | Update timestamp   |

---

### `character_notes`

| Column        | Type | Constraints                                      | Description |
| ------------- | ---- | ------------------------------------------------ | ----------- |
| note\_id      | UUID | FK to `notes(id)`, ON DELETE CASCADE             | Note        |
| character\_id | UUID | FK to `player_characters(id)`, ON DELETE CASCADE | Character   |

**Primary Key:** (note\_id, character\_id)

---

### `npc_notes`

| Column     | Type | Constraints                          | Description |
| ---------- | ---- | ------------------------------------ | ----------- |
| note\_id   | UUID | FK to `notes(id)`, ON DELETE CASCADE | Note        |
| npc\_id    | UUID | FK to `npcs(id)`, ON DELETE CASCADE  | NPC         |
| author\_id | UUID | FK to `users(id)`, ON DELETE CASCADE | Author      |

**Primary Key:** (note\_id, npc\_id)

---

### `calendar_notes`

| Column         | Type         | Constraints                     | Description           |
| -------------- | ------------ | ------------------------------- | --------------------- |
| id             | UUID         | PK                              | Event identifier      |
| title          | VARCHAR(255) | NOT NULL                        | Event title           |
| description    | TEXT         |                                 | Event description     |
| game\_datetime | TIMESTAMP    |                                 | In-game date and time |
| is\_exam       | BOOLEAN      | Default FALSE                   | Exam flag             |

---

### `event_notes`

| Column     | Type | Constraints                                   | Description |
| ---------- | ---- | --------------------------------------------- | ----------- |
| note\_id   | UUID | FK to `notes(id)`, ON DELETE CASCADE          | Note        |
| event\_id  | UUID | FK to `calendar_notes(id)`, ON DELETE CASCADE | Event       |
| author\_id | UUID | FK to `users(id)`, ON DELETE CASCADE          | Author      |

**Primary Key:** (note\_id, event\_id)

---

### `stores`

| Column      | Type         | Constraints                     | Description       |
| ----------- | ------------ | ------------------------------- | ----------------- |
| id          | UUID         | PK                              | Store identifier  |
| name        | VARCHAR(255) | NOT NULL                        | Store name        |
| location    | VARCHAR(255) |                                 | Store location    |
| description | TEXT         |                                 | Store description |
| image\_url  | TEXT         |                                 | Store image URL   |

---

### `store_items`

| Column      | Type          | Constraints                           | Description           |
| ----------- | ------------- | ------------------------------------- | --------------------- |
| id          | UUID          | PK                                    | Store item identifier |
| store\_id   | UUID          | FK to `stores(id)`, ON DELETE CASCADE | Associated store      |
| name        | VARCHAR(255)  | NOT NULL                              | Item name             |
| description | TEXT          |                                       | Item description      |
| price       | DECIMAL(10,2) |                                       | Item price            |
| image\_url  | TEXT          |                                       | Item image URL        |

---

### `books`

| Column     | Type         | Constraints                     | Description     |
| ---------- | ------------ | ------------------------------- | --------------- |
| id         | UUID         | PK                              | Book identifier |
| title      | VARCHAR(255) | NOT NULL                        | Book title      |
| summary    | TEXT         |                                 | Book summary    |
| section    | VARCHAR(255) |                                 | Book section    |
| is\_hidden | BOOLEAN      | Default FALSE                   | Hidden flag     |
| image\_url | TEXT         |                                 | Book image URL  |

---

### `news`

| Column         | Type         | Constraints                     | Description           |
| -------------- | ------------ | ------------------------------- | --------------------- |
| id             | UUID         | PK                              | News identifier       |
| headline       | VARCHAR(255) | NOT NULL                        | News headline         |
| body           | TEXT         |                                 | News body             |
| game\_datetime | TIMESTAMP    |                                 | In-game date and time |
| image\_url     | TEXT         |                                 | News image URL        |

---

### `maps`

| Column     | Type         | Constraints                     | Description    |
| ---------- | ------------ | ------------------------------- | -------------- |
| id         | UUID         | PK                              | Map identifier |
| title      | VARCHAR(255) | NOT NULL                        | Map title      |
| image\_url | TEXT         |                                 | Map image URL  |

---

### `monsters`

| Column             | Type         | Constraints                     | Description        |
| ------------------ | ------------ | ------------------------------- | ------------------ |
| id                 | UUID         | PK                              | Monster identifier |
| name               | VARCHAR(255) | NOT NULL                        | Monster name       |
| hit\_points        | INT          |                                 | Hit points         |
| experience\_points | INT          |                                 | Experience points  |
| strength           | INT          |                                 | Strength           |
| dexterity          | INT          |                                 | Dexterity          |
| constitution       | INT          |                                 | Constitution       |
| intelligence       | INT          |                                 | Intelligence       |

---

### `sessions`

| Column      | Type      | Constraints   | Description                  |
| ----------- | --------- | ------------- | ---------------------------- |
| session\_id | TEXT      | PRIMARY KEY   | Unique session identifier    |
| user\_id    | UUID      | NOT NULL      | Reference to the user        |
| created\_at | TIMESTAMP | DEFAULT NOW() | Session creation timestamp   |
| expires\_at | TIMESTAMP | NOT NULL      | Session expiration timestamp |

## Mermaid Diagram

erDiagram
    %% =========================
    %% USERS & AUTHENTICATION
    %% =========================
    USERS {
        uuid id PK
        string name
        string email
        string password
        enum role
        text avatar_url
    }

    SESSIONS {
        string session_id PK
        uuid user_id FK
        timestamp created_at
        timestamp expires_at
    }

    %% =========================
    %% CAMPAIGN STRUCTURE
    %% =========================
    COLLEGES {
        uuid id PK
        string name
        text description
        text image_url
    }

    CLASSES {
        uuid id PK
        string name
        text description
        uuid college_id FK
        text image_url
    }

    PLAYER_CHARACTERS {
        uuid id PK
        uuid user_id FK
        string name
        text image_url
        int college_year
        uuid college_id FK
        text enrolled_classes
        int level
    }

    CHARACTER_SHEET {
        uuid id PK
        uuid character_id FK
        int strength
        int dexterity
        int constitution
        int intelligence
        int wisdom
        int charisma
        int proficiency_bonus
        int armor_class
        int initiative
        numeric speed
        int max_hit_points
        int current_hit_points
        int temp_hit_points
        int hit_dice_total
        int hit_dice_current
        int save_str
        int save_dex
        int save_con
        int save_int
        int save_wis
        int save_cha
        text skills
        text background
        text race
        text alignment
        int experience_points
        text languages
        text features_traits
        text proficiencies
        text description
        timestamp created_at
        timestamp updated_at
    }

    %% =========================
    %% INVENTORY & ITEMS
    %% =========================
    INVENTORY_ITEMS {
        uuid id PK
        uuid character_id FK
        uuid item_id
        int amount
        jsonb metadata
    }

    %% =========================
    %% NPCs & REPUTATION
    %% =========================
    NPCS {
        uuid id PK
        string name
        text image_url
        text bio
        boolean is_visible
        text visible_to
    }

    NPCS_REPUTATION {
        uuid id PK
        uuid character_id FK
        uuid npc_id FK
        int score
    }

    %% =========================
    %% NOTES SYSTEM
    %% =========================
    NOTES {
        uuid id PK
        uuid author_id FK
        text content
        boolean is_master_only
        boolean is_privative
        timestamp created_at
        timestamp updated_at
    }

    CHARACTER_NOTES {
        uuid note_id FK
        uuid character_id FK
    }

    NPC_NOTES {
        uuid note_id FK
        uuid npc_id FK
        uuid author_id FK
    }

    CALENDAR_NOTES {
        uuid id PK
        string title
        text description
        timestamp game_datetime
        boolean is_exam
    }

    EVENT_NOTES {
        uuid note_id FK
        uuid event_id FK
        uuid author_id FK
    }

    %% =========================
    %% STORES & STORE ITEMS
    %% =========================
    STORES {
        uuid id PK
        string name
        string location
        text description
        text image_url
    }

    STORE_ITEMS {
        uuid id PK
        uuid store_id FK
        string name
        text description
        decimal price
        text image_url
    }

    %% =========================
    %% BOOKS & NEWS
    %% =========================
    BOOKS {
        uuid id PK
        string title
        text summary
        string section
        boolean is_hidden
        text image_url
    }

    NEWS {
        uuid id PK
        string headline
        text body
        timestamp game_datetime
        text image_url
    }

    %% =========================
    %% MAPS & MONSTERS
    %% =========================
    MAPS {
        uuid id PK
        string title
        text image_url
    }

    MONSTERS {
        uuid id PK
        string name
        int hit_points
        int experience_points
        int strength
        int dexterity
        int constitution
        int intelligence
        int wisdom
        int charisma
        int armor_class
        text description
        text image_url
    }

    %% =========================
    %% RELATIONSHIPS
    %% =========================
    USERS ||--o{ PLAYER_CHARACTERS : "has"
    USERS ||--o{ NOTES : "writes"
    USERS ||--o{ NPC_NOTES : "writes"
    USERS ||--o{ EVENT_NOTES : "writes"
    USERS ||--o{ SESSIONS : "owns"

    COLLEGES ||--o{ CLASSES : "offers"
    COLLEGES ||--o{ PLAYER_CHARACTERS : "attended by"

    CLASSES ||--o{ PLAYER_CHARACTERS : "enrolled in"

    PLAYER_CHARACTERS ||--o{ INVENTORY_ITEMS : "owns"
    PLAYER_CHARACTERS ||--o{ CHARACTER_SHEET : "has"
    PLAYER_CHARACTERS ||--o{ NPCS_REPUTATION : "interacts with"
    PLAYER_CHARACTERS ||--o{ CHARACTER_NOTES : "has"

    NPCS ||--o{ NPCS_REPUTATION : "linked to"
    NPCS ||--o{ NPC_NOTES : "has notes"

    CALENDAR_NOTES ||--o{ EVENT_NOTES : "linked to"

    NOTES ||--o{ CHARACTER_NOTES : "relates to"
    NOTES ||--o{ NPC_NOTES : "relates to"
    NOTES ||--o{ EVENT_NOTES : "relates to"

    STORES ||--o{ STORE_ITEMS : "sells"

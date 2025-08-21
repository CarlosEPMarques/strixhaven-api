CREATE TYPE user_role AS ENUM ('DM', 'PLAYER');

CREATE TABLE users (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role user_role NOT NULL,
    avatar_url TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE colleges (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE books (
    id UUID PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    summary TEXT,
    section VARCHAR(100),
    language VARCHAR(50),
    is_hidden BOOLEAN DEFAULT FALSE,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE maps (
    id UUID PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    image_url TEXT
);

CREATE TABLE monsters (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    size VARCHAR(50),
    alignment VARCHAR(50),
    armor_class INT,
    hit_points INT,
    speed VARCHAR(50),
    abilities JSONB,
    actions JSONB,
    experience_points INT,
    strength INT,
    dexterity INT,
    constitution INT,
    intelligence INT,
    wisdom INT,
    charisma INT,
    description TEXT,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE news (
    id UUID PRIMARY KEY,
    headline VARCHAR(100) NOT NULL,
    body TEXT,
    game_datetime TIMESTAMP,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE stores (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    description TEXT,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE calendar_notes (
    id UUID PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    game_datetime TIMESTAMP,
    is_exam BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE npcs (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    college_id UUID REFERENCES colleges(id) ON DELETE SET NULL,
    college_year INT,
    image_url TEXT,
    bio TEXT,
    is_visible BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE player_characters (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    image_url TEXT,
    college_year INT,
    college_id UUID REFERENCES colleges(id) ON DELETE SET NULL,
    level INT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE classes (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    college_id UUID REFERENCES colleges(id) ON DELETE SET NULL,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE grades (
    id UUID PRIMARY KEY,
    character_id UUID REFERENCES player_characters(id) ON DELETE CASCADE,
    class_id UUID REFERENCES classes(id) ON DELETE CASCADE,
    score INT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (character_id, class_id)
);

CREATE TABLE quests (
    id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    responsible_npc UUID REFERENCES npcs(id) ON DELETE SET NULL,
    active BOOLEAN DEFAULT TRUE,
    rewards JSONB,
    expire_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE store_items (
    id UUID PRIMARY KEY,
    store_id UUID REFERENCES stores(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2),
    image_url TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE character_sheet (
    id UUID PRIMARY KEY,
    character_id UUID UNIQUE REFERENCES player_characters(id) ON DELETE CASCADE,
    strength INTEGER,
    dexterity INTEGER,
    constitution INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    proficiency_bonus INTEGER,
    armor_class INTEGER,
    initiative INTEGER,
    speed INTEGER,
    max_hit_points INTEGER,
    current_hit_points INTEGER,
    temp_hit_points INTEGER,
    hit_dice_total INTEGER,
    hit_dice_current INTEGER,
    save_str INTEGER,
    save_dex INTEGER,
    save_con INTEGER,
    save_int INTEGER,
    save_wis INTEGER,
    save_cha INTEGER,
    skills JSONB,
    background TEXT,
    race TEXT,
    alignment TEXT,
    experience_points INTEGER,
    languages JSONB,
    features_traits JSONB,
    proficiencies JSONB,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE spells (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    level INT,
    cast_modes JSONB,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE stories (
    id,
    title,
    content,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
)

CREATE TABLE student_scoreboard (
    id UUID PRIMARY KEY,
    ranking INT,
    student_name VARCHAR(100),
    student_college VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE inventory_items (
    id UUID PRIMARY KEY,
    character_id UUID REFERENCES player_characters(id) ON DELETE CASCADE,
    item_id UUID REFERENCES store_items(id) ON DELETE SET NULL,
    amount INT,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (character_id, item_id)
);

CREATE TABLE npcs_reputation (
    id UUID PRIMARY KEY,
    character_id UUID REFERENCES player_characters(id) ON DELETE CASCADE,
    npc_id UUID REFERENCES npcs(id) ON DELETE CASCADE,
    score INT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (character_id, npc_id)
);

CREATE TABLE notes (
    id UUID PRIMARY KEY,
    author_id UUID REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(150),
    content TEXT NOT NULL,
    is_master_only BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE character_notes (
    note_id UUID REFERENCES notes(id) ON DELETE CASCADE,
    character_id UUID REFERENCES player_characters(id) ON DELETE CASCADE,
    PRIMARY KEY (note_id, character_id)
);

CREATE TABLE npc_notes (
    note_id UUID REFERENCES notes(id) ON DELETE CASCADE,
    npc_id UUID REFERENCES npcs(id) ON DELETE CASCADE,
    author_id UUID REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (note_id, npc_id)
);


CREATE TABLE npc_visibility (
    npc_id UUID REFERENCES npcs(id) ON DELETE CASCADE,
    player_id UUID REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (npc_id, player_id)
);

CREATE TABLE character_classes (
    character_id UUID REFERENCES player_characters(id) ON DELETE CASCADE,
    class_id UUID REFERENCES classes(id) ON DELETE CASCADE,
    PRIMARY KEY (character_id, class_id)
);
